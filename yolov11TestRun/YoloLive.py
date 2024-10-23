import cv2
import torch
from ultralytics import YOLO

# Load the YOLOv11 model
model = YOLO('yolo11n.pt')
results = model(0, show=True, stream= True)

for result in results:
    boxes = result.boxes
    classes = result.names