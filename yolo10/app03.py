from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO("last.pt")

# Run inference on 'bus.jpg' with arguments
model.predict("aa.jpg", save=True, imgsz=320, conf=0.5)