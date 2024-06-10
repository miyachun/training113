
# Load YOLOv8n-seg, train it on COCO128-seg for 3 epochs and predict an image with it
from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')  # load a pretrained YOLOv8n segmentation model

model.train(data='fruit.yaml', epochs=10)  # train the model
model('aa.jpg')  # predict on an image