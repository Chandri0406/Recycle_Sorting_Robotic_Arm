from ultralytics import YOLO

#Load a model
model = YOLO("yolo11n.pt")  

# Train the model
model.train(data="data.yaml", epochs=100, imgsz=64, batch=8, workers=1, device="cpu")