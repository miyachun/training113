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
yolo10->https://github.com/THU-MIG/yolov10/tree/main  
Predict:yolo predict model=yolov8n.pt source='https://ultralytics.com/images/zidane.jpg'  
Train model:yolov8n.pt data=coco8.yaml epochs=3 imgsz=640  
Train model:yolov8n.pt data=XXX.yaml epochs=20 imgsz=640  


