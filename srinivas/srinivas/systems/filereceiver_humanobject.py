# from imageai.Detection import ObjectDetection
from PIL import Image 
import io
# from numpy import asarray
import base64
from wsgiref import headers
import requests
# import json
import os
import uuid
from asyncio import sleep
from wsgiref import headers
import requests
import time
from datetime import datetime
import paho.mqtt.client as paho
from modules import invoke_api_sendemail

current_datetime = datetime.now()
str_current_datetime = str(current_datetime)


def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed --- : " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, message):
   
    # i = 1
    id = uuid.uuid1()
    # current_datetime = datetime.now()
    # str_current_datetime = str(current_datetime)
    # file_name = "/home/administrator/srinivas/Part2/Mqtt Coding session/Mqttflow/compressedimagesfrompi/compressedimages"+ str(i)+"$"+str_current_datetime+".jpg"
    # i =i+1

    # f = open(file_name, 'wb')
    # # f = open('classificationimages.jpg', 'wb')
    # f.write(message.payload)
    # print(f)
    # f.close()
   
    image_data = message.payload
    image = Image.open(io.BytesIO(image_data))
    
    # Decompress in memory
    with io.BytesIO() as output:
        
        
        i=1
        # image.save(output,format= "JPEG", quality =100)
        contents = output.getvalue()
        # Invoke mqttextracthuman faas api
        invoke_api_sendemail(contents)
        backup = "/home/angel/srinivas/backupimages/extracthumanobject" + str(id)+"$" + str_current_datetime+".jpg"
      
        i=i+1
        b = open(backup, 'wb')
        b.write(image_data)
        print(b)
        b.close()



if __name__ == "__main__":

    #mqttBroker = "10.5.1.89"
    #mqttBroker = "192.168.49.1"
    mqttBroker = "localhost"
    port = 1883
    c=paho.Client("")
    c.connect(mqttBroker, port)

    print("listening")
    i = 1

    c.on_message = on_message
    c.on_subscribe = on_subscribe

    c.subscribe("/testmqtt/extracthuman",2) 

    # Second subscriber code 
  

    c.loop_start() 

    time.sleep(3000)

    c.loop_stop()
