-相關-  
Raspberry Pi Imager->https://www.raspberrypi.com/software/  
PuTTY->https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html  
VNC Viewer->https://www.realvnc.com/en/connect/download/viewer/  
pi4 gpio->https://images.theengineeringprojects.com/image/webp/2021/03/raspberry-pi-4.png.webp?ssl=1  


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
