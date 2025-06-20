# Helmet Detection in CT Scans

## Project Overview
Streamlit web application for detecting helmets in CT scans using:
- YOLOv8 (ultralytics)
- Faster R-CNN (detectron2)

## Features
- Upload CT scan images (JPG/PNG)
- Select between two detection models
- Adjust confidence threshold
- Visualize detections with bounding boxes
- Display detection statistics

## Installation
1. Clone repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the Streamlit app:
```bash
streamlit run app/streamlit_app.py
```

## Models
1. **YOLOv8**
   - Pretrained on custom helmet dataset
   - Optimized for real-time detection

2. **Faster R-CNN**
   - Detectron2 implementation
   - Higher accuracy but slower

## Output
- Original and annotated images
- Detection counts:
  - With helmet
  - Without helmet