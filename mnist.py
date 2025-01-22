# -*- coding: utf-8 -*-
"""MNIST.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZyGqiGRskEw-NiKblzxs_8l7yjyZVHAA
"""

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import numpy as np
import matplotlib.pyplot as plt

# dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalization: 0-255 to 0-1
x_train = x_train / 255.0
x_test = x_test / 255.0

# data visualization
plt.figure(figsize=(10, 5))
for i in range(12):
    plt.subplot(3, 4, i + 1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f"Label: {y_train[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()

# starting the model
model = Sequential([
    Flatten(input_shape=(28, 28)),  # 28x28
    Dense(128, activation='relu'),  # first hidden layer
    Dense(10, activation='softmax')  # output layer
])

# Modeli compile
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()  # Model summary

# Model train
history = model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# performance on data set
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")

# few predictions
predictions = model.predict(x_test)

# visualize
plt.figure(figsize=(10, 5))
for i in range(12):
    plt.subplot(3, 4, i + 1)
    plt.imshow(x_test[i], cmap='gray')
    plt.title(f"True: {y_test[i]}, Pred: {np.argmax(predictions[i])}")
    plt.axis('off')
plt.tight_layout()
plt.show()

# Save model
model.save("mnist_model.h5")
print("Model saved successfully.")

from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# lad model
model = load_model("mnist_model.h5")

# name of the png doc
image_path = "digit.png"  # rename it

# process the figure
image = Image.open(image_path).convert('L')  # black-white
image = image.resize((28, 28))  # 28x28
image_array = np.array(image)
image_array = 255 - image_array
image_array = image_array / 255.0  # Normalization

# visualize
plt.imshow(image_array, cmap='gray')
plt.title("Yüklenen Görsel")
plt.axis('off')
plt.show()

# predict
image_array = np.expand_dims(image_array, axis=0)  # (1, 28, 28)
predicted_probs = model.predict(image_array)
predicted_label = np.argmax(predicted_probs)

print(f"Model prediction: {predicted_label}")