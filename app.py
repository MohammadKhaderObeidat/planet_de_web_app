import streamlit as st
import tensorflow as tf
from tensorflow.keras import models, layers
import numpy as np
from PIL import Image
import os

# Set page configuration
st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿",
    layout="centered",
)

# Custom CSS for plant-themed colors
st.markdown("""
    <style>
    .main {
        background-color: #f0f5f0;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
    }
    .stHeader {
        color: #2e7d32;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 Plant Disease Detection System")
st.write("AI-powered classification for Potato and Tomato crops.")

# Constants from notebook
IMAGE_SIZE = 256
CLASS_NAMES = [
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Tomato_Bacterial_spot',
    'Tomato__Tomato_YellowLeaf__Curl_Virus',
    'Tomato_healthy'
]

# Sidebar for information
with st.sidebar:
    st.header("About")
    st.write("This app uses a Convolutional Neural Network (CNN) to detect diseases in potato and tomato leaves.")
    st.write("### Supported Classes:")
    for name in CLASS_NAMES:
        st.write(f"- {name.replace('_', ' ')}")

# Function to load model
@st.cache_resource
def load_trained_model():
    # In a real scenario, we'd load a saved .keras file.
    # For this demo, we'll define the architecture from the notebook.
    model = models.Sequential([
        layers.Input(shape=(IMAGE_SIZE, IMAGE_SIZE, 3)),
        layers.Resizing(IMAGE_SIZE, IMAGE_SIZE),
        layers.Rescaling(1./255),
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Dropout(0.2),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(len(CLASS_NAMES), activation='softmax')
    ])
    
    # Try to load weights if they exist
    if os.path.exists("plant_model.keras"):
        model.load_weights("plant_model.keras")
    elif os.path.exists("potato_model.keras"):
        # Note: This is a simplification since the notebook shows one model for both
        model.load_weights("potato_model.keras")
        
    return model

model = load_trained_model()

# Image uploader
uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    # Preprocess the image
    img_array = np.array(image.resize((IMAGE_SIZE, IMAGE_SIZE)))
    img_batch = np.expand_dims(img_array, 0)
    
    # Prediction button
    if st.button('Predict'):
        with st.spinner('Analyzing...'):
            predictions = model.predict(img_batch)
            predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
            confidence = np.max(predictions[0])
            
            # Display results
            st.success(f"Prediction: **{predicted_class.replace('_', ' ')}**")
            st.info(f"Confidence: **{confidence:.2%}**")
            
            # Advice based on prediction
            if "healthy" in predicted_class.lower():
                st.balloons()
                st.write("Your plant looks healthy! Keep up the good work.")
            else:
                st.warning("Detection suggests a disease. Please consult with an agricultural expert for treatment options.")

st.divider()
st.caption("Note: This is a demonstration app. For accurate diagnosis, please ensure the image is clear and focused on a single leaf.")
