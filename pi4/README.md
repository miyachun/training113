-相關-  
Raspberry Pi Imager->https://www.raspberrypi.com/software/  
設定裡面填入相關訊息  

PuTTY->https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html  
host name for ip address->raspberrypi.local  
port->22  

VNC Viewer->https://www.realvnc.com/en/connect/download/viewer/  
pi4 gpio->https://images.theengineeringprojects.com/image/webp/2021/03/raspberry-pi-4.png.webp?ssl=1  


-Virtualenv-  
python -m venv .myenv  
source .myenv/bin/activate  

-MQTT Pi4-  
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
 
-DHT11 DHT22-  
Python Setup  
https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup  
Installing the CircuitPython-DHT Library  
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi  

![image](https://github.com/miyachun/training113/blob/main/pi4/demo.jpg)  


