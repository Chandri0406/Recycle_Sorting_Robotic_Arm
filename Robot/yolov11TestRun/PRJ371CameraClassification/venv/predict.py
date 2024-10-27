from ultralytics import YOLO
import cv2
import torch

# Load our custom model
model = YOLO("C:/Users/chanb/OneDrive/Documents/GitHub/Recycle_Sorting_Robotic_Arm/Robot/yolov11TestRun/PRJ371CameraClassification/runs/classify/train2/weights/best.pt")
results = model(0, show=True, stream= True)

for result in results:
    boxes = result.boxes
    classes = result.names