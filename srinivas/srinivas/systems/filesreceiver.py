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
from modules import invoke_api_extracthunamobject

 
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed --- : " + str(mid) + " " + str(granted_qos))


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
    image.save("resized_image.png")
    # with open("/home/administrator/Contribution-3/connect-to-mqtt/resized_image.png", "rb") as image:
    #     f = image.read()
    #     b = bytearray(f)


    with open("resized_image.png", "rb") as image:
        f = image.read()
        b = bytearray(f)
        print("resize image store")
        #print(b)
        invoke_api_extracthunamobject(b)
        print("After invokation of extracthuman function")
    # print("HHFGH")
    # with io.BytesIO() as output:
    #     contents = output.getvalue()
    #     invoke_api_extracthunamobject(contents)
    #     # print(contents)
    #     print("After invokation of extracthuman function")
    
    # with open("got-the-image.png", "rb") as image:
    #     f = image.read()
    #     b = bytearray(f)
    # resized_image=image.resize((640,640))
    # resized_image.save("resized_image.png")
    # print(resized_image.height, resized_image.width, 'H * W')
    # with open("resized_image.png", "rb") as image:
    # f = image.read()
    # b = bytearray(f)
    # invoke_api_extracthunamobject(b)
   

    #Decompress in memory
    # with io.BytesIO() as output:
    #     print("hi")
    #     #image.save(output,format= "JPEG", quality =100)
        
    #     contents = output.getvalue()
    #     print(resized_image.height, resized_image.width, 'H * W')
    #     #image.save(file_name, contents)
    #     #Invoke mqttextracthuman faas api
    #     invoke_api_extracthunamobject(contents)
    #     print("After invokation")
    #     # Subscriber to the topic

      




if __name__ == "__main__":


    mqttBroker = "192.168.49.1"
    #mqttBroker = "localhost"
    port = 1883
    c=paho.Client("")
    c.connect(mqttBroker, port)

    print("listening")


    c.on_message = on_message
    c.on_subscribe = on_subscribe

    c.subscribe("/testmqtt/frompi",2) 

    # Second subscriber code 
  

    c.loop_start() 

    time.sleep(3000)

    c.loop_stop()
    
