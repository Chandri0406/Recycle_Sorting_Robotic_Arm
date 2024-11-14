from ultralytics import YOLO
from imutils.video import FPS
import cv2
import serial
import time

# Load our custom model
model = YOLO("../runs/detect/train2/weights/best.pt")

ser = serial.Serial("COM13", 9600, timeout=1)

# Start video stream and FPS counter
cap = cv2.VideoCapture(1)
cooldown = 40

lastDetectedTime = time.time()

detectedTime = 5

detectedInFrame = None

currentLabel = None

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
    "cardboard": 'A\n',
    "glass": 'B\n',
    "metal": 'C\n',
    "paper": 'D\n',
    "plastic": 'E\n',
}

sortedMaterials = []

while True:
    success, frame = cap.read()
    if not success:
        break

    results = model(frame, stream=True)
    currentTime = time.time()
    detectedInFrame = False

    if currentTime - lastDetectedTime > cooldown:

        # Extract bounding boxes from results
        for result in results:
            boxes = result.boxes
            for box in boxes:
                cls_id = int(box.cls[0].item())
                label = model.names[cls_id] if cls_id < len(model.names) else "Unknown"
                confidence = box.conf[0].item()

                # Display bounding box and label on frame
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                if confidence >= 0.40 and label == "cardboard":
                    # Increment count for detected material
                    material_counts['cardboard'] += 1

                    # Send material ID via UART
                    ser.write(b'A\n')
                    print(f"Sent ID {materialIDS[label]} for {label}")
                    lastDetectedTime = currentTime
                    detectedInFrame = None

                    # Display bounding box and label on frame
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                
                elif confidence >= 0.40 and label == "glass":
                    # Increment count for detected material
                    material_counts[label] += 1

                        # Send material ID via UART
                    ser.write(b'B\n')
                    print(f"Sent ID {materialIDS[label]} for {label}")
                    lastDetectedTime = currentTime
                    detectedInFrame = None

                        # Display bounding box and label on frame
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                elif confidence >= 0.40 and label == "metal":
                    # Increment count for detected material
                    material_counts[label] += 1

                        # Send material ID via UART
                    ser.write(b'C\n')
                    print(f"Sent ID {materialIDS[label]} for {label}")
                    lastDetectedTime = currentTime
                    detectedInFrame = None

                        # Display bounding box and label on frame
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                elif confidence >= 0.40 and label == "paper":
                    # Increment count for detected material
                    material_counts[label] += 1

                    # Send material ID via UART
                    ser.write(b'D\n')
                    print(f"Sent ID {materialIDS[label]} for {label}")
                    lastDetectedTime = currentTime
                    detectedInFrame = None

                    # Display bounding box and label on frame
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                elif confidence >= 0.40 and label == "plastic":
                    #Increment count for detected material
                    material_counts[label] += 1

                    # Send material ID via UART
                    ser.write(b'E\n')
                    print(f"Sent ID {materialIDS[label]} for {label}")
                    lastDetectedTime = currentTime
                    detectedInFrame = None

                    # Display bounding box and label on frame
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                

                else:
                    if detectedInFrame and (time.time() - detectedInFrame) >= detectedTime:
                        ser.write(b'F\n')
                        print(f"Failed to send ID {materialIDS[label]}")
                        lastDetectedTime = currentTime
                        detectedInFrame = None

    # Display frame
    cv2.imshow("Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    fps.update()

# Cleanup
fps.stop()
cap.release()
cv2.destroyAllWindows()

print(f"Sorted Materials: {material_counts}")