import os
import streamlit as st

# Set UTF-8 encoding for the entire application
os.environ["PYTHONIOENCODING"] = "utf-8"
from inference import load_model, predict
from utils import visualize_detections

st.set_page_config(page_title="Helmet Detection", layout="wide")
st.title("🔒 Helmet Detection in CT Scans")

# Sidebar controls
with st.sidebar:
    st.header("Settings")
    model_type = st.radio(
        "Select Model",
        ["YOLOv8", "Faster R-CNN"],
        index=0
    )
    confidence = st.slider(
        "Confidence Threshold", 
        min_value=0.1, 
        max_value=0.9, 
        value=0.5,
        step=0.1
    )

# Main content
uploaded_file = st.file_uploader(
    "Upload CT Scan Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Display original image
    st.image(uploaded_file, caption="Original Image", use_column_width=True)

    # Load model and predict
    model = load_model(model_type)
    detections = predict(model, uploaded_file, confidence)

    # Visualize results
    result_img = visualize_detections(uploaded_file, detections, model_type)
    st.image(result_img, caption="Detection Results", use_column_width=True)