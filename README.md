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
Raspberry Pi Imager->https://www.raspberrypi.com/software/  
PuTTY->https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html  
VNC Viewer->https://www.realvnc.com/en/connect/download/viewer/  
pi4 gpio->https://images.theengineeringprojects.com/image/webp/2021/03/raspberry-pi-4.png.webp?ssl=1  


-raspberry 指令-  
sudo apt update  
sudo apt upgrade  
sudo raspi-config  
sudo apt-get install mosquitto mosquitto-clients  
sudo systemctl enable mosquitto.service  
sudo nano /etc/mosquitto/mosquitto.conf  
listener 1883  
allow_anonymous true  
sudo reboot  

ifconfig  
pip install 'paho-mqtt<2.0.0'  
pip install rpi.gpio
