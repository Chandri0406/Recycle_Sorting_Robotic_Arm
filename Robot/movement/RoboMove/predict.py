from ultralytics import YOLO
import cv2
import torch
#from move.py import detect_and_sort

# Load our custom model
model = YOLO("../runs/detect/train3/weights/best.pt")
results = model(0, show=True, stream= True)

for result in results:
    boxes = result.boxes
    classes = result.names

#detect_and_sort(results)