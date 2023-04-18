import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model('mnv2_glassesornoglasses.h5')


# Define the class names
class_names = ['glasses', 'no_glasses'] # Replace with your own class names

# Define the function for making predictions
def predict(image):
    # Load and preprocess the image
    image = image.resize((160, 160))
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Make predictions
    preds = model.predict(img_array)
    class_idx = np.argmax(preds[0])
    class_name = class_names[class_idx]

    return class_name



# Define the Streamlit app

st.title("Image Classifier")
st.write("This app predicts the class of an input image.")

# Create a file uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# If an image is uploaded, make predictions and display the image and predicted class
if uploaded_file is not None:
    # Load the image
    img = Image.open(uploaded_file)

    # Make predictions
    class_name = predict(img)

    # Display the image and predicted class
    st.image(img, caption=f"Predicted class: {class_name}", use_column_width=True)