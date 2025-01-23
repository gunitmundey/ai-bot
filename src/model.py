from tensorflow import keras
from tensorflow.keras import layers
import logging

def create_model(input_shape):
    model = keras.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=input_shape))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1, activation='linear'))  # Output layer for regression

    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_model(model, x_train, y_train, epochs=50, batch_size=32):
    try:
        model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)
        logging.info("Model training completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during model training: {e}")

def evaluate_model(model, x_test, y_test):
    try:
        evaluation = model.evaluate(x_test, y_test)
        logging.info("Model evaluation completed successfully.")
        return evaluation
    except Exception as e:
        logging.error(f"An error occurred during model evaluation: {e}")
        return None