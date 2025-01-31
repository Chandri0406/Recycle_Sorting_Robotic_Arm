from ultralytics import YOLO
import cv2
import torch

# Load our custom model
model = YOLO("../runs/detect/train2/weights/best.pt")
results = model(1, show=True, stream= True)

for result in results:
    boxes = result.boxes
    classes = result.names