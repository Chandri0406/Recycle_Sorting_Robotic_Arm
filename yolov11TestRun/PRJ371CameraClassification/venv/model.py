from ultralytics import YOLO

#Load a model
model = YOLO("yolo11n-cls.pt")  

# Train the model
results = model.train(data="C:/Users/divan/Desktop/PRJ371CameraClassification/PRJDataset", epochs=100, imgsz=64)