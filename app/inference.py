import os
from ultralytics import YOLO
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2 import model_zoo
import torch
import cv2
from PIL import Image
import numpy as np

MODEL_PATHS = {
    "YOLOv8": "Models/yolov8m_best.pt",
    "Faster R-CNN": "Models/detectron_best.pth"
}

CLASS_NAMES = ["Without Helmet", "With Helmet"]

def load_model(model_type: str):
    """Load either YOLOv8 or Faster R-CNN model"""
    if model_type == "YOLOv8":
        model = YOLO(MODEL_PATHS["YOLOv8"])
        return model
    else:
        cfg = get_cfg()
        # Exact config from training
        cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
        cfg.MODEL.WEIGHTS = MODEL_PATHS["Faster R-CNN"]
        
        # Verify weights file exists
        if not os.path.exists(cfg.MODEL.WEIGHTS):
            raise FileNotFoundError(f"Model weights not found at {cfg.MODEL.WEIGHTS}")
            
        cfg.MODEL.ROI_HEADS.NUM_CLASSES = 2
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
        cfg.MODEL.DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Training parameters
        cfg.DATALOADER.NUM_WORKERS = 2
        cfg.SOLVER.IMS_PER_BATCH = 4
        cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 128
        
        predictor = DefaultPredictor(cfg)
        print(f"✅ Model loaded successfully from {cfg.MODEL.WEIGHTS}")
        print(f"Model architecture: {cfg.MODEL.META_ARCHITECTURE}")
        print(f"Number of classes: {cfg.MODEL.ROI_HEADS.NUM_CLASSES}")
        
        return predictor

def predict(model, image_file, confidence: float = 0.5):
    """Run inference on uploaded image"""
    img = Image.open(image_file)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    img_array = np.array(img)
    
    if isinstance(model, YOLO):
        results = model.predict(
            source=img_array,
            conf=confidence,
            classes=[0, 1]  # Only helmet classes
        )
        return results[0]
    else:
        outputs = model(img_array)
        # Debug output
        print("Model outputs:", outputs)
        print("Detected classes:", outputs["instances"].pred_classes)
        print("Scores:", outputs["instances"].scores)
        
        filtered = outputs["instances"][outputs["instances"].scores > confidence]
        print("Filtered instances count:", len(filtered))
        
        return {
            "instances": filtered
        }