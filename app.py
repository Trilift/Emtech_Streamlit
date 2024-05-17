import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the saved model
model = tf.keras.models.load_model('mnist_cnn_model.h5')

# Define a function to preprocess the image
def preprocess_image(image):
    # Convert the image to grayscale
    image = image.convert('L')
    # Resize the image to 28x28
    image = image.resize((28, 28))
    # Convert the image to numpy array
    image_array = np.array(image) / 255.0
    # Reshape the array to match the model input shape
    image_array = image_array.reshape((1, 28, 28, 1))
    return image_array

# Streamlit app
st.title('Digit Recognition Algorithm')
st.write('by Paulo Abregrunda and Nikko Denila')
st.image("number.jpg", width=400)
st.write("""
        This application can determine what number is shown in the image uploaded.
        \n These numbers can range from 0-9.
        """)

uploaded_image = st.file_uploader("Upload an image here", type=["jpg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Preprocess the image
    if len(np.array(image).shape) == 3:  # Check if the image is 3D
        # Convert the RGB image to grayscale
        image = image.convert('L')
        # Resize the image to 28x28
        image = image.resize((28, 28))
        # Convert the image to numpy array
        image_array = np.array(image) / 255.0
        # Reshape the array to match the model input shape
        preprocessed_image = image_array.reshape((1, 28, 28, 1))
    else:
        # If the image is already grayscale, directly preprocess it
        preprocessed_image = preprocess_image(image)

    # Make prediction
    prediction = model.predict(preprocessed_image)

    # Display the prediction
    st.write('The number in the image is:', np.argmax(prediction))
