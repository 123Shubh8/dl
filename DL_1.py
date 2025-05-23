# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pehJC2KUIAbkAxoV0HFtjCZwSvx7yAJQ
"""

# Import necessary libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Embedding, Flatten
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Set the number of words to use (top N words)
num_words = 10000
max_len = 500  # maximum length of review

# Load IMDB dataset
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=num_words)

# Pad sequences to ensure all reviews have the same length
X_train = pad_sequences(X_train, maxlen=max_len)
X_test = pad_sequences(X_test, maxlen=max_len)

# Define the model
model = Sequential()

# Adding the embedding layer
model.add(Embedding(input_dim=num_words, output_dim=128, input_length=max_len))

# Add a Flatten layer to flatten the output of the Embedding layer to a 1D array
model.add(Flatten())

# Adding a fully connected layer with ReLU activation
model.add(Dense(512, activation='relu'))

# Add a dropout layer to prevent overfitting
model.add(Dropout(0.5))

# Add a fully connected output layer with 1 unit for binary classification
model.add(Dense(1, activation='sigmoid'))  # Sigmoid activation for binary classification

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Print the model summary to check the architecture
model.summary()

# Train the model
history = model.fit(X_train, y_train, epochs=3, batch_size=64, validation_data=(X_test, y_test))

# Evaluate the model
score = model.evaluate(X_test, y_test, batch_size=64)
print(f"Test loss: {score[0]}")
print(f"Test accuracy: {score[1]}")

# Commented out IPython magic to ensure Python compatibility.
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from tqdm.notebook import tqdm
import warnings
warnings.filterwarnings("ignore")

boston = tf.keras.datasets.boston_housing

dir(boston)

boston_data = boston.load_data()

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

x_train.shape, y_train.shape, x_test.shape, y_test.shape

scaler = StandardScaler()

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

model = Sequential([
    Input(shape=(x_train_scaled.shape[1],)),  # Input layer (recommended approach)
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='linear')  # Linear activation for regression
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train the model
history = model.fit(x_train_scaled, y_train, validation_split=0.2, epochs=100, verbose=1)

# Evaluate the model on the test set
loss, mae = model.evaluate(x_test_scaled, y_test, verbose=0)
print(f"Test MAE: {mae}")

# Predict on the test set
y_pred = model.predict(x_test_scaled)

# Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)

print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("Mean Absolute Error:", mae)

# Inverse transform predictions and actual values
y_pred = y_scaler.inverse_transform(y_pred_scaled)
y_actual = y_scaler.inverse_transform(y_test_scaled)

# Plot: Regression line
plt.figure(figsize=(8,6))
sns.regplot(x=y_actual.flatten(), y=y_pred.flatten(), scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Regression Line for Predicted Values")
plt.show()

import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import warnings
warnings.filterwarnings("ignore")

boston = tf.keras.datasets.boston_housing

dir(boston)

boston_data = boston.load_data()

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

x_train.shape, y_train.shape, x_test.shape, y_test.shape

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

model = Sequential([
    Input(shape=(x_train_scaled.shape[1],)),  # Input layer (recommended approach)
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='linear')  # Linear activation for regression
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train the model
history = model.fit(x_train_scaled, y_train, validation_split=0.2, epochs=100, verbose=1)

# Evaluate the model on the test set
loss, mae = model.evaluate(x_test_scaled, y_test, verbose=0)
print(f"Test MAE: {mae}")

# Predict on the test set
y_pred = model.predict(x_test_scaled)

# Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)

print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("Mean Absolute Error:", mae)

y_scaler = StandardScaler()  # Add this new scaler only for y

y_train_scaled = y_scaler.fit_transform(y_train.reshape(-1, 1))
y_test_scaled = y_scaler.transform(y_test.reshape(-1, 1))

y_pred_scaled = model.predict(x_test_scaled)
y_pred = y_scaler.inverse_transform(y_pred_scaled)
y_actual = y_scaler.inverse_transform(y_test_scaled)

plt.figure(figsize=(8,6))
sns.regplot(x=y_actual.flatten(), y=y_pred.flatten(), scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Regression Line for Predicted Values")
plt.show()

