from ultralytics import YOLO
import cv2
import time
from sharedData import materialCounts

# Load our custom model
model = YOLO("../runs/detect/train5/weights/best.pt")

cap = cv2.VideoCapture(0)

cooldown = 20

lastDetectedTime = time.time()
while True:
    success, frame = cap.read()
    results = model(frame, stream=True)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls_id = int(box.cls[0].item())
            label = model.names[cls_id] if cls_id < len(model.names) else "Unknown"
            currentTime = time.time()

            if currentTime - lastDetectedTime > cooldown:
                materialCounts[label] += 1

        # Display frame
    cv2.imshow("Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
print(f"Sorted Materials: {materialCounts}")