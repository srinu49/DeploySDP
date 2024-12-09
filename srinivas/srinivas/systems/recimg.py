import paho.mqtt.client as mqtt
import base64
from io import BytesIO
from PIL import Image

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the topic where the image will be published
    client.subscribe("/testmqtt/frompi")

def on_message(client, userdata, msg):
    print("Received message")
    try:
        # Decode base64-encoded image data
        decoded_image = base64.b64decode(msg.payload)

        # Convert the image data to a PIL Image
        image = Image.open(BytesIO(decoded_image))

        # Do something with the image (e.g., display or save it)
        image.show()
        

    except Exception as e:
        print(f"Error processing image: {e}")

# Set up the MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Replace "10.5.1.153" with the IP address of your MQTT broker
mqtt_broker = "10.5.1.153"
mqtt_port = 1883  # Default MQTT port

# Connect to the MQTT broker
client.connect(mqtt_broker, mqtt_port,60)

# Start the MQTT loop to receive messages
client.loop_forever()

