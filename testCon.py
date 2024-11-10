from ultralytics import YOLO
import cv2
import torch
import serial
#from move import detectAndSort

ser = serial.Serial("COM9", 9600)

# Load our custom model
model = YOLO("../runs/detect/train3/weights/best.pt")
results = model(1, show=True, stream= True)

for result in results:
    boxes = result.boxes
    classes = result.names

    for box in boxes:
        detectedClass = classes[int(box.cls.item())]
        
        # Send detected class name or ID to the microcontroller
        ser.write(f"{detectedClass}\n".encode())  # Send data as bytes with newline for separation
        print(f"Sent {detectedClass} to microcontroller")
    #detectAndSort(result)

ser.close