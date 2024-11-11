from ultralytics import YOLO
from imutils.video import FPS
import cv2
import serial

# Load our custom model
model = YOLO("../runs/detect/train2/weights/best.pt")

ser = serial.Serial("COM9", 9600)

# Start video stream and FPS counter
cap = cv2.VideoCapture(1)

#setting width and heigh of camera
cap.set(3, 640)
cap.set(4, 480)

fps = FPS().start()

# Setting counts of materials (now stores frame counts for each material)
material_counts = {
    "cardboard": 0,
    "glass": 0,
    "metal": 0,
    "paper": 0,
    "plastic": 0,
}

materialIDS = {
    "cardboard": 0,
    "glass": 1,
    "metal": 2,
    "paper": 3,
    "plastic": 4,
}

sortedMaterials = []

while True:
    success, frame = cap.read()
    if not success:
        break

    results = model(frame, stream=True)

    # Extract bounding boxes from results
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls_id = int(box.cls[0].item())  # Class ID of detected object
            label = model.names[cls_id] if cls_id < len(model.names) else "Unknown"
            confidence = box.conf[0].item()

            if confidence >= 0.85 and label in materialIDS:
                # Increment count for detected material
                material_counts[label] += 1

                # Send material ID via UART
                ser.write(bytes([materialIDS[label]]))
                print(f"Sent ID {materialIDS[label]} for {label}")

            # Display bounding box and label on frame
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display frame
    cv2.imshow("Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    fps.update()

# Cleanup
fps.stop()
cap.release()
cv2.destroyAllWindows()

print(f"Sorted Materials: {sortedMaterials}")