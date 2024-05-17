# -*- coding: utf-8 -*-
"""streamlit_app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gr7J7uBvJsYsE0JmIwIr-GR9OY7ntF8f
"""

import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the model
model = tf.keras.models.load_model('cnn_cifar10.h5')

# Define class names
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Streamlit app title
st.title("Image Classification with CIFAR-10")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Convert the file to an image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Preprocess the image
    img = image.resize((32, 32))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict the class
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    st.write(f"This image is most likely a {class_names[np.argmax(score)]} with a {100 * np.max(score):.2f}% confidence.")
