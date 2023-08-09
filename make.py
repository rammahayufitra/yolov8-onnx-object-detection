from ultralytics import YOLO 
model = YOLO("yolov8s.pt")  
results = model.predict(source="https://ultralytics.com/images/bus.jpg")[0]
model.export(format="onnx",opset=12)