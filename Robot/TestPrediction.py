from ultralytics import YOLO
import cv2
import time
#from sharedData import materialCounts

# Load our custom model
model = YOLO("../runs/detect/train/weights/best.pt")

cap = cv2.VideoCapture(1)

cooldown = 20

lastDetectedTime = time.time()

materialCounts = {
    "cardboard": 0,
    "glass": 0,
    "metal": 0,
    "paper": 0,
    "plastic": 0,
}

while True:
    success, frame = cap.read()
    results = model(frame, stream=True)
    currentTime = time.time()
    

    for result in results:
        boxes = result.boxes

        if currentTime - lastDetectedTime > cooldown:
            for box in boxes:
                cls_id = int(box.cls[0].item())
                label = model.names[cls_id] if cls_id < len(model.names) else "Unknown"
                

                materialCounts[label] += 1

        # Display frame
    cv2.imshow("Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
print(f"Sorted Materials: {materialCounts}")