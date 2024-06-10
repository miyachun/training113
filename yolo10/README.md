-虛擬環境安裝-  
 
1->環境變數  
C:\XXX\Programs\Python\Python310\Scripts  
C:\XXX\Programs\Python\Python310  
  
2->安裝virtualenv  
pip install virtualenv  
virtualenv 取一個名稱  
  
3->啟動  
到虛擬環境Scripts目錄中啟動  
activate  



-相關-  
virtualenv->virtualenv -p python3.10 XXX  
smeshariks dataset->https://universe.roboflow.com/khalina/smeshariks  
yolo10->https://github.com/THU-MIG/yolov10/tree/main  
https://docs.ultralytics.com/tasks/  
Predict:yolo predict model=yolov8n.pt source='https://ultralytics.com/images/zidane.jpg'  
Train:yolo train model=yolov8n.pt data=coco8.yaml epochs=3 imgsz=640  
segment:yolo segment predict model=yolov8n-seg.pt source='https://ultralytics.com/images/bus.jpg'  # predict with official model  
segment:yolo segment predict model=path/to/best.pt source='https://ultralytics.com/images/bus.jpg'  # predict with custom model  



