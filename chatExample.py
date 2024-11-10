from ultralytics import YOLO
import cv2
import serial
import time
import math
from imutils.video import FPS
from DanielCode import *

# Initialize material counts
material_counts = { "cardboard": 0, "glass": 0, "metal": 0, "paper": 0, "plastic": 0 }

# Serial communication setup
ser = serial.Serial("COM9", 9600)
ser.flushInput()
pico_responses = ["Done Moving\r\n", "Connected to Pico\r\n"]

# Load YOLO model
model = YOLO("../runs/detect/train7/weights/best.pt")  # Update path as needed

# Start video stream and FPS counter
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
time.sleep(2)
fps = FPS().start()

done = 1

while True:
    success, frame = cap.read()
    if not success:
        break

    # YOLO detection
    results = model(frame, stream=True)
    for result in results:
        boxes = result.boxes  # YOLO result boxes
        for box in boxes:
            # Get class label and confidence
            cls_id = int(box.cls[0])
            label = model.names[cls_id] if cls_id < len(model.names) else "Unknown"
            confidence = math.ceil(box.conf[0] * 100) / 100

            # Draw bounding box and label on frame
            (x1, y1, x2, y2) = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Call the specific method based on the label and confidence
            if confidence >= 0.85:
                if label.lower() == "metal":
                    PickUpMetal()
                elif label.lower() == "paper":
                    PickUpPaper()
                elif label.lower() == "plastic":
                    PickUpPlastic()
                elif label.lower() == "glass":
                    PickUpGlass()
                elif label.lower() == "cardboard":
                    PickUpCardboard()

    # Communication with Pico
    if ser.inWaiting() > 0:
        pico_response = ser.readline().decode().strip()
        if pico_response in pico_responses:
            done = 1

    # Display frame
    cv2.imshow("Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    fps.update()

# Cleanup
fps.stop()
cap.release()
cv2.destroyAllWindows()
