import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):  # The callback for when 
    print("Connected with result code {0}".format(str(rc)))
    # Print result of connection attempt client.subscribe("digitest/test1")  
    # Subscribe to the topic “digitest/test1”, receive any messages 


def on_message(client, userdata, msg):  # The callback for when a PUBLISH 
    print("Message received-> " + msg.topic + " " + str(msg.payload))

MQTT_BROKER = 'io.adafruit.com'
MQTT_PORT = 1883
ADAFRUIT_IO_USERNAME = 'jparshook'   # Replace with your Adafruit IO username
ADAFRUIT_IO_KEY = 'aio_pQCI91TyV3iHZovMtPwbRQQ1FELa'         # Replace with your Adafruit IO key
client = mqtt.Client()  # Create instance of client with client ID “digi_mqtt_test”
client.on_connect = on_connect  # Define callback function for successful connection
client.on_message = on_message  # Define callback function for receipt of a message
# client.connect("m2m.eclipse.org", 1883, 60)  # Connect to (broker, port, keepalive-time)
client.username_pw_set(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.connect(MQTT_BROKER, MQTT_PORT, 10)
client.loop_forever()  # Start networking daemon