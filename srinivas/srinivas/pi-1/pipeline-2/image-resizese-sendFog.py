#Image Resize Code
from PIL import Image 
import base64
from wsgiref import headers
import requests
# import json
import os
import io
# import uuid
from asyncio import sleep
from wsgiref import headers
import requests
import time
from datetime import datetime
import paho.mqtt.client as paho
# from modules import invoke_api_extracthunamobject

 
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed --- : " + str(mid) + " " + str(granted_qos))


def publish_to_broker(image_content):
    client = paho.Client("tcp://192.168.49.1:1883", transport="tcp")
    broker = "all_words[0]"
    port = 1883
    client.connect(broker, port)
    client.loop_start() 
    client.publish("/testmqtt/frompi", image_content,2)
    print("published resized image on to the desktop 10.5.0.54 and topic name is /testmqtt/frompi")
    #time.sleep(10)
    client.loop_stop()

def on_message(client, userdata, message):
   
    # i = 1
    # current_datetime = datetime.now()
    # str_current_datetime = str(current_datetime)
    # file_name = "/home/administrator/srinivas/Part2/Mqtt Coding session/Mqttflow/compressedimagesfrompi/compressedimages"+ str(i)+"$"+str_current_datetime+".jpg"
    # i =i+1
    #file_name ="/home/administrator/srinivas/Part2/Mqtt Coding session/Mqttflow/decompressed"
    # f = open(file_name, 'wb')
    # # f = open('classificationimages.jpg', 'wb')
    # f.write(message.payload)
    # print(f)
    # f.close()
    image_data = message.payload
    image = Image.open(io.BytesIO(image_data))

    with io.BytesIO() as output:
        resized_image=image.resize((640,640))
        print("Image Resized into H * W", resized_image.height, resized_image.width)
        resized_image.save(output, format='JPEG')
        contents = output.getvalue()
        publish_to_broker(contents)


    # resized_image=image.resize((640,640))
    # resized_image.save("resized_image.png")

all_words = []
    with open("pi_ipadd.txt", "r") as file:
    # Read each line
    for line in file:
        # Split the line into words
        words = line.strip().split(',')
        # Add the words to the list
        all_words.extend(words)
    file.close()

if __name__ == "__main__":

    
    mqttBroker = "all_words[0]"
    port = 1883
    c=paho.Client("")
    c.connect(mqttBroker, port)

    print("listening")


    c.on_message = on_message
    c.on_subscribe = on_subscribe

    c.subscribe("/testmqtt/compress",2) 

    # Second subscriber code 
  

    c.loop_start() 

    time.sleep(2)

    c.loop_stop()
    
