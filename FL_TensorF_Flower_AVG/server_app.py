"""Flower ServerApp for Federated Learning.

This module implements the ServerApp with FedAvg strategy.
"""

from flwr.app import ArrayRecord
from flwr.serverapp import ServerApp, Grid, Context
from flwr.serverapp.strategy import FedAvg

from .task import get_model_by_type


# Create ServerApp instance
app = ServerApp()


@app.main()
def main(grid: Grid, context: Context) -> None:
    """Main entry point for the ServerApp.
    
    Args:
        grid: Grid object for interfacing with client nodes
        context: Context with run configuration
    """
    # Load configuration
    num_rounds = context.run_config["num-server-rounds"]
    fraction_train = context.run_config.get("fraction-train", 1.0)
    fraction_evaluate = context.run_config.get("fraction-evaluate", 1.0)
    min_fit_clients = context.run_config.get("min-fit-clients", 2)
    min_evaluate_clients = context.run_config.get("min-evaluate-clients", 2)
    min_available_clients = context.run_config.get("min-available-clients", 2)
    
    # Model configuration
    model_type = context.run_config["model-type"]
    input_shape = context.run_config["input-shape"]
    num_classes = context.run_config.get("num-classes", 1)
    learning_rate = context.run_config.get("learning-rate", 0.001)
    
    # Load initial model
    model = get_model_by_type(model_type, input_shape, num_classes, learning_rate)
    arrays = ArrayRecord(model.get_weights())
    
    # Define and start FedAvg strategy
    strategy = FedAvg(
        fraction_train=fraction_train,
        fraction_evaluate=fraction_evaluate,
        min_fit_clients=min_fit_clients,
        min_evaluate_clients=min_evaluate_clients,
        min_available_clients=min_available_clients,
    )
    
    # Start federated learning
    result = strategy.start(
        grid=grid,
        initial_arrays=arrays,
        num_rounds=num_rounds,
    )
    
    # Save the final model
    print(f"\n📊 Federated Learning completed for {model_type}")
    print(f"   Total rounds: {num_rounds}")
    
    # Return result for further processing
    return result
