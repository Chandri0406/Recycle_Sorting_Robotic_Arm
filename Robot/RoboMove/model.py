from ultralytics import YOLO

#Load a model
model = YOLO("yolo11m.pt")  

# Train the model
model.train(data="data.yaml", epochs=200, imgsz=640, batch=8, workers=1, device="cpu")