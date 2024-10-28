from ultralytics import YOLO

#Load a model
model = YOLO("yolo11n.pt")  

# Train the model
results = model.train(data="C:/Users/chanb/OneDrive/Documents/GitHub/Recycle_Sorting_Robotic_Arm/Robot/yolov11TestRun/PRJ371CameraClassification/PRJDataset", epochs=100, imgsz=64)