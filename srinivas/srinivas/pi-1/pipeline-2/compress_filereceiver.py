from PIL import Image 
import os
import io
from asyncio import sleep
import time
from datetime import datetime
import paho.mqtt.client as mqtt
#from libcompress import image_compress, sendimages_tomqttbroker 

all_words = []
    with open("pi_ipadd.txt", "r") as file:
    # Read each line
    for line in file:
        # Split the line into words
        words = line.strip().split(',')
        # Add the words to the list
        all_words.extend(words)
    file.close()

def publish_to_broker(image_content):
    client = mqtt.Client("tcp://192.168.49.1:1883", transport="tcp")
    broker = "all_words[0]"
    port = 1883
    client.connect(broker, port)
    client.loop_start() 
    client.publish("/testmqtt/compress", image_content,2)
    print("Image has been compressed and published into /testmqtt/compress topic")
    #time.sleep(10)
    client.loop_stop()

def on_message(client, userdata, message):
    """ 
    Receive the message.payload from the broker, reduce the file size and publish it to the broker
    """
    image_data = message.payload
    image = Image.open(io.BytesIO(image_data))
    print(image.height, image.width, "H x W original image is going to be compressed")
    # compressing in-memory
    with io.BytesIO() as output:
        image.save(output, format='JPEG',optimize = True, quality = 40)
        contents = output.getvalue()
        publish_to_broker(contents)
        #client.publish("/testmqtt/frompi", contents)
    
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed --- : " + str(mid) + " " + str(granted_qos))


# mqttBroker = "mqtt.eclipseprojects.io"
#client = mqtt.Client("tcp://192.168.49.1:1883", transport="tcp")
#mqttBroker = "10.5.0.170" #10.5.0.170

if __name__ == "__main__":
	# configurations
	mqttBroker = "all_words[0]"
	port = 1883
	client=mqtt.Client("")
	client.connect(mqttBroker, port)

	print("listening")
	# c.subscribe("/testmqtt/classification1") 
	i = 1
	# setting event handlers
	client.on_message = on_message
	client.on_subscribe = on_subscribe

	# c.subscribe("/testmqtt/pushimage1")   #change this

	client.subscribe("/testmqtt/frompi",2) 
	#import compressimage
	client.loop_start() 
	time.sleep(2)
	client.loop_stop()

