"""Task definitions for Federated Learning with ToN-IoT Dataset.

This module contains model definitions, data loading, and training functions.
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Dense, Dropout, Flatten, Conv1D, MaxPooling1D, 
    Input, BatchNormalization
)
from tensorflow.keras.regularizers import l2


def load_model_mlp_binary(input_shape: int, learning_rate: float = 0.001):
    """Create MLP model for binary classification.
    
    Args:
        input_shape: Number of input features
        learning_rate: Learning rate for Adam optimizer
        
    Returns:
        Compiled Keras model
    """
    model = Sequential([
        Dense(256, activation='relu', input_shape=(input_shape,), 
              kernel_regularizer=l2(0.001)),
        BatchNormalization(),
        Dropout(0.3),
        Dense(128, activation='relu', kernel_regularizer=l2(0.001)),
        Dropout(0.3),
        Dense(64, activation='relu'),
        Dropout(0.2),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    return model


def load_model_cnn_binary(input_shape: int, learning_rate: float = 0.001):
    """Create CNN model for binary classification.
    
    Args:
        input_shape: Number of input features
        learning_rate: Learning rate for Adam optimizer
        
    Returns:
        Compiled Keras model
    """
    model = Sequential([
        Input(shape=(input_shape, 1)),
        Conv1D(64, 3, activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling1D(2),
        Conv1D(32, 3, activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling1D(2),
        Conv1D(16, 3, activation='relu', padding='same'),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.4),
        Dense(64, activation='relu'),
        Dropout(0.3),
        Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    return model


def load_model_mlp_multi(input_shape: int, num_classes: int, 
                         learning_rate: float = 0.001):
    """Create MLP model for multi-class classification.
    
    Args:
        input_shape: Number of input features
        num_classes: Number of output classes
        learning_rate: Learning rate for Adam optimizer
        
    Returns:
        Compiled Keras model
    """
    model = Sequential([
        Dense(512, activation='relu', input_shape=(input_shape,), 
              kernel_regularizer=l2(0.002)),
        BatchNormalization(),
        Dropout(0.4),
        Dense(256, activation='relu', kernel_regularizer=l2(0.002)),
        Dropout(0.4),
        Dense(128, activation='relu'),
        Dropout(0.3),
        Dense(64, activation='relu'),
        Dropout(0.2),
        Dense(num_classes, activation='softmax')
    ])
    
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model


def load_model_cnn_multi(input_shape: int, num_classes: int, 
                        learning_rate: float = 0.001):
    """Create CNN model for multi-class classification.
    
    Args:
        input_shape: Number of input features
        num_classes: Number of output classes
        learning_rate: Learning rate for Adam optimizer
        
    Returns:
        Compiled Keras model
    """
    model = Sequential([
        Input(shape=(input_shape, 1)),
        Conv1D(128, 3, activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling1D(2),
        Conv1D(64, 3, activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling1D(2),
        Conv1D(32, 3, activation='relu', padding='same'),
        BatchNormalization(),
        Flatten(),
        Dense(256, activation='relu'),
        Dropout(0.5),
        Dense(128, activation='relu'),
        Dropout(0.4),
        Dense(64, activation='relu'),
        Dropout(0.3),
        Dense(num_classes, activation='softmax')
    ])
    
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model


def get_model_by_type(model_type: str, input_shape: int, 
                      num_classes: int = 1, learning_rate: float = 0.001):
    """Factory function to get model by type.
    
    Args:
        model_type: One of ['mlp_binary', 'cnn_binary', 'mlp_multi', 'cnn_multi']
        input_shape: Number of input features
        num_classes: Number of output classes (1 for binary)
        learning_rate: Learning rate for optimizer
        
    Returns:
        Compiled Keras model
    """
    model_mapping = {
        'mlp_binary': lambda: load_model_mlp_binary(input_shape, learning_rate),
        'cnn_binary': lambda: load_model_cnn_binary(input_shape, learning_rate),
        'mlp_multi': lambda: load_model_mlp_multi(input_shape, num_classes, learning_rate),
        'cnn_multi': lambda: load_model_cnn_multi(input_shape, num_classes, learning_rate)
    }
    
    if model_type not in model_mapping:
        raise ValueError(f"Unknown model type: {model_type}. "
                        f"Choose from {list(model_mapping.keys())}")
    
    return model_mapping[model_type]()
