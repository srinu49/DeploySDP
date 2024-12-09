import paho.mqtt.client as mqtt
import base64

mqtt_topic ="/testmqtt/frompi"

broker = "10.5.1.153"
port =1883

def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe(mqtt_topic)

def on_message(client,userdata,msg):

    print("Received message")
    try:
        # Decode base64-encoded image data
        decoded_image = base64.b64decode(msg.payload)

        # Specify the file path where you want to save the image
        file_path = "resize_image.png"

        # Save the image data to the specified file
        with open(file_path, "wb") as image_file:
            image_file.write(decoded_image)

        # Optionally, you can open the image using PIL
        image = Image.open(file_path)
        image.show()

    except Exception as e:
        print(f"Error processing image: {e}")









    # print("Image received")
    # with ("resize_image.png", "wb") as image_file:
    #     image_file.write(msg.payload)
    # print("image saved")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)

client.loop_forever()


