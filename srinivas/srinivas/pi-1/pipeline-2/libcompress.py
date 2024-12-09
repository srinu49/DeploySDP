import time
from datetime import datetime
import os
from PIL import Image
import paho.mqtt.client as mqtt

base_dir = "/home/pi/srinivas/picameraimages/"

mqttBroker = "localhost"
port = 1883
client=mqtt.Client("")
client.connect(mqttBroker, port)

def image_compress():
	current_datetime = datetime.now()
	str_current_datetime = str(current_datetime)
	i = 1
	images = os.listdir(base_dir)
	print("found "+ str(len(images)) + " files")
	for file in images:
		
		image = Image.open(base_dir + file)

		image.save("/home/pi/srinivas/compressedimages/image-file-compressed" + str(i) + '$'+ str_current_datetime, 
                 "JPEG", 
                 optimize = True, 
                 quality = 40)
		i = i + 1
		os.remove(base_dir + file)
		
		
def sendimages_tomqttbroker():
    images = os.listdir("/home/pi/srinivas/compressedimages")
    for file in images:
    	f=open("/home/pi/srinivas/compressedimages/"+file, "rb")
    	ImageContent=f.read()
    	print("found "+ str(len(images)) + " files")
    	#client.publish("/testmqtt/frompi", ImageContent)
    	f.close()
    	os.remove("/home/pi/srinivas/compressedimages/" + file)
    	print("published an image")
		
