import os
import time
from picamera import PiCamera

from datetime import datetime

import paho.mqtt.client as mqtt
#from module import publish_images
# broker = address of the mosquitto where we want to send an image

def publish_images():
    print("connected to my lab")
    client = mqtt.Client("tcp://192.168.49.1:1883", transport="tcp")

    broker = "10.5.0.209"  

    port = 1883

    client.connect(broker, port)

    client.loop_start() 

    print("Starting")
    images = os.listdir("/home/pi/srinivas/picameraimages")

    for file in images:
        f=open("/home/pi/srinivas/picameraimages/"+file, "rb")
        ImageContent=f.read()
        client.publish("/testmqtt/frompi", ImageContent,2 )
        os.remove("/home/pi/srinivas/picameraimages/" + file)
        print("published an image")



FOLDER_NAME = "/home/pi/srinivas/picameraimages"
BACK_UP = "/home/pi/srinivas/backupimages"

if not os.path.exists(FOLDER_NAME):
    os.mkdir(FOLDER_NAME)

camera = PiCamera()
camera.resolution = (1280, 720)
camera.rotation = 180
#time.sleep(5)

current_datetime = datetime.now()
str_current_datetime = str(current_datetime)

counter = 1
   
while counter < 50:
    file_name = FOLDER_NAME + "/img" + str(counter) + str_current_datetime + ".jpg"
    backup = BACK_UP + "/img" + str(counter) + str_current_datetime + ".jpg"
    counter += 1
        
    camera.capture(file_name)
    camera.capture(backup)
    #camera.capture(file_name, use_video_port=True)
    print("New photo has been taken")
    publish_images()
    #import sendimagestomqttbroker
   # time.sleep(3)
camera.close()                          

  
  
          
