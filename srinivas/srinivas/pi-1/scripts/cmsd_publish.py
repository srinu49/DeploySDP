import paho.mqtt.client as mqtt
from PIL import Image 
import os
import io
from asyncio import sleep
import time
from datetime import datetime

# MQTT settings
#mqtt_topic = "/testmqtt/frompi"
#broker = "10.5.1.153"
#port = 1883
all_words = []
with open("/opt/human-detection/sys_ipadd.txt", "r") as file:
    # Read each line
    for line in file:
        # Split the line into words
        words = line.strip().split(',')
        # Add the words to the list
        all_words.extend(words)
    file.close()

def publish_to_broker(image_content):
    client = mqtt.Client("tcp://192.168.49.1:1883", transport="tcp")
    broker = all_words[0]
    port = 1883
    client.connect(broker, port)
    client.loop_start() 
    client.publish("/testmqtt/frompi", image_content,2)
    print("Image has been resized and published into /testmqtt/frompi topic on the cmsd node")
    #time.sleep(10)
    client.loop_stop()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

#client = mqtt.Client()
#client.on_connect = on_connect
#client.connect(broker, port, 60)

#client.loop_start()



image = Image.open("/opt/human-detection/resized_image.png")

image_bytes = io.BytesIO()
image.save(image_bytes, format='JPEG')
image_bytes = image_bytes.getvalue()
publish_to_broker(image_bytes)
print("called publisher")

#print(image.height, image.width, "H x W original image is going to be compressed")
    # compressing in-memory
#with io.BytesIO() as output:
    #image.save(output, format='JPEG',optimize = True, quality = 40)
    #contents = output.getvalue()
    #publish_to_broker(contents)

# Path to your image file
#image_path = "resized_image.png"

#with open(image_path, "rb") as image_file:
    #image_data = image_file.read()
    #client.publish(mqtt_topic, payload=image_data, qos=2)
    #print("Image sent to angel")
    


