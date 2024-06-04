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

-開通win防火牆1883埠-  
設定/隱私權與安全性/Windows安全性/開啟windows安全性/防火牆與網路保護/進階設定/點左方輸入規則/再點右方的新增規則/選擇[連接埠]/下一步/選擇[TCP]/選擇[特定本機連接埠]/輸入1883/下一步/允許連線/下一步接續完成。



