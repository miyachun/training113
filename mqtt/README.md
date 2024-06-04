-相關-  
virtualenv->virtualenv -p python3.10 XXX  
mqtt window server->https://mosquitto.org/download/?source=post_page-----741b655708ff--------------------------------  



-MQTT Window Server-  
1->下載 mqtt window server  
2->開啟工作管理員/服務/mosquitto(右鍵啟動)，狀態(執行中)  
3->修改 config 檔案  
位置 : C:\Program Files\mosquitto\mosquitto.conf  
加入 :  
allow_anonymous true  
listener 1883 172.20.10.2  # ip address  

在當地目錄下開啟cmd並輸入以下  
mosquitto -c mosquitto.conf -v  

