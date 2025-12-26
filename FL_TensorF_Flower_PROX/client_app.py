"""Flower ClientApp for Federated Learning with FedProx.

This module implements the ClientApp with train and evaluate methods
using the FedProx algorithm with proximal term.
"""

import numpy as np
from flwr.app import ClientApp, Message, Context
from flwr.app import ArrayRecord, RecordDict, MetricRecord
import keras

from .task import get_model_by_type, ProximalModel


# Create ClientApp instance
app = ClientApp()


@app.train()
def train(msg: Message, context: Context):
    """Train the model on local data using FedProx algorithm.
    
    Args:
        msg: Message containing model weights and configuration
        context: Context with run configuration and node information
        
    Returns:
        Message with updated model weights and training metrics
    """
    # Reset local TensorFlow state
    keras.backend.clear_session()
    
    # Get configuration from context
    model_type = context.run_config["model-type"]
    input_shape = context.run_config["input-shape"]
    num_classes = context.run_config.get("num-classes", 1)
    learning_rate = context.run_config.get("learning-rate", 0.001)
    local_epochs = context.run_config.get("local-epochs", 1)
    batch_size = context.run_config.get("batch-size", 256)
    verbose = context.run_config.get("verbose", 0)
    mu = context.run_config.get("mu", 0.01)  # FedProx proximal term coefficient
    
    # Get client data from node config
    partition_id = context.node_config["partition-id"]
    X_train = context.node_config["X_train"]
    y_train = context.node_config["y_train"]
    
    # Convert to numpy arrays if needed
    if not isinstance(X_train, np.ndarray):
        X_train = np.array(X_train)
    if not isinstance(y_train, np.ndarray):
        y_train = np.array(y_train)
    
    # Ensure proper data types
    X_train = X_train.astype(np.float32)
    
    # For CNN models, reshape input
    if 'cnn' in model_type:
        X_train = X_train.reshape(-1, input_shape, 1)
    
    # Get global model weights from message
    global_weights = msg.content["arrays"].to_numpy_ndarrays()
    
    # Load the base model
    base_model = get_model_by_type(model_type, input_shape, num_classes, learning_rate)
    base_model.set_weights(global_weights)
    
    # Wrap with ProximalModel to add proximal term
    proximal_model = ProximalModel(base_model, global_weights, mu)
    
    # Determine loss function based on task type
    loss_fn = 'binary_crossentropy' if num_classes == 1 else 'sparse_categorical_crossentropy'
    
    # Compile the proximal model
    proximal_model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss=loss_fn,
        metrics=['accuracy']
    )
    
    # Train the model with proximal term
    history = proximal_model.fit(
        X_train,
        y_train,
        epochs=local_epochs,
        batch_size=batch_size,
        verbose=verbose,
    )
    
    # Get training metrics
    train_loss = history.history["loss"][-1] if "loss" in history.history else None
    train_acc = (
        history.history["accuracy"][-1] if "accuracy" in history.history else None
    )
    
    # Pack model weights and metrics into message
    # Extract weights from the base model (not the wrapper)
    model_record = ArrayRecord(proximal_model.model.get_weights())
    metrics = {"num-examples": len(X_train)}
    
    if train_loss is not None:
        metrics["train_loss"] = train_loss
    if train_acc is not None:
        metrics["train_acc"] = train_acc
    
    content = RecordDict({"arrays": model_record, "metrics": MetricRecord(metrics)})
    
    return Message(content=content, reply_to=msg)


@app.evaluate()
def evaluate(msg: Message, context: Context):
    """Evaluate the model on local validation data.
    
    Args:
        msg: Message containing model weights
        context: Context with run configuration and node information
        
    Returns:
        Message with evaluation metrics
    """
    # Reset local TensorFlow state
    keras.backend.clear_session()
    
    # Get configuration from context
    model_type = context.run_config["model-type"]
    input_shape = context.run_config["input-shape"]
    num_classes = context.run_config.get("num-classes", 1)
    learning_rate = context.run_config.get("learning-rate", 0.001)
    batch_size = context.run_config.get("batch-size", 256)
    verbose = context.run_config.get("verbose", 0)
    
    # Get client data from node config
    X_test = context.node_config.get("X_test")
    y_test = context.node_config.get("y_test")
    
    if X_test is None or y_test is None:
        # No test data provided, return empty metrics
        metrics = {}
        content = RecordDict({"metrics": MetricRecord(metrics)})
        return Message(content=content, reply_to=msg)
    
    # Convert to numpy arrays if needed
    if not isinstance(X_test, np.ndarray):
        X_test = np.array(X_test)
    if not isinstance(y_test, np.ndarray):
        y_test = np.array(y_test)
    
    # Ensure proper data types
    X_test = X_test.astype(np.float32)
    
    # For CNN models, reshape input
    if 'cnn' in model_type:
        X_test = X_test.reshape(-1, input_shape, 1)
    
    # Load the model
    model = get_model_by_type(model_type, input_shape, num_classes, learning_rate)
    
    # Set weights from message
    model.set_weights(msg.content["arrays"].to_numpy_ndarrays())
    
    # Evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test, batch_size=batch_size, verbose=verbose)
    
    # Pack metrics into message
    metrics = {
        "num-examples": len(X_test),
        "eval_loss": loss,
        "eval_acc": accuracy
    }
    
    content = RecordDict({"metrics": MetricRecord(metrics)})
    
    return Message(content=content, reply_to=msg)
