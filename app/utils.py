# -*- coding: utf-8 -*-
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def visualize_detections(image_file, detections, model_type: str):
    """Visualize detections with bounding boxes"""
    img = Image.open(image_file)
    img_array = np.array(img)
    
    if model_type == "YOLOv8":
        # Custom visualization to match Faster R-CNN colors
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        boxes = detections.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            score = box.conf[0]
            class_id = int(box.cls[0])
            class_label = "With Helmet" if class_id == 1 else "Without Helmet"
            label = f"{class_label} {score:.2f}"
            color = (0, 255, 0) if class_id == 1 else (0, 0, 255)  # Green for helmet, red for no helmet
            
            cv2.rectangle(img_array, (x1, y1), (x2, y2), color, 2)
            cv2.putText(
                img_array, label, (x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2
            )
        
        return Image.fromarray(cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB))
    else:
        # Faster R-CNN custom visualization
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        for box, score, class_id in zip(
            detections["instances"].pred_boxes,
            detections["instances"].scores,
            detections["instances"].pred_classes
        ):
            x1, y1, x2, y2 = box.int().cpu().numpy()
            class_label = "With Helmet" if class_id == 1 else "Without Helmet"
            label = f"{class_label} {score:.2f}"
            color = (0, 255, 0) if class_id == 1 else (0, 0, 255)  # Green for helmet, red for no helmet
            
            cv2.rectangle(img_array, (x1, y1), (x2, y2), color, 2)
            cv2.putText(
                img_array, label, (x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2
            )
        
        return Image.fromarray(cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB))

def get_detection_stats(detections, model_type: str):
    """Calculate detection statistics"""
    if model_type == "YOLOv8":
        boxes = detections.boxes
        helmet_count = sum(boxes.cls == 1)
        no_helmet_count = sum(boxes.cls == 0)
    else:
        instances = detections["instances"]
        helmet_count = sum(instances.pred_classes == 1)
        no_helmet_count = sum(instances.pred_classes == 0)
    
    return {
        "total": helmet_count + no_helmet_count,
        "with_helmet": helmet_count,
        "without_helmet": no_helmet_count
    }