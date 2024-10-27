from ultralytics import YOLO

#Load a model
model = YOLO("yolo11n-cls.pt")  

# Train the model
results = model.train(data="./yolov11TestRun/PRJ371CameraClassification/PRJDataset", epochs=100, imgsz=64)