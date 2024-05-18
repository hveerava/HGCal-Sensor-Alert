import paho.mqtt.client as mqtt

# Adafruit IO credentials
ADAFRUIT_IO_USERNAME = 'jparshook'   # Replace with your Adafruit IO username
ADAFRUIT_IO_KEY = 'aio_pQCI91TyV3iHZovMtPwbRQQ1FELa'         # Replace with your Adafruit IO key

# MQTT broker settings
MQTT_BROKER = 'io.adafruit.com'
MQTT_PORT = 1883

# Feed names
FEED_TEMPERATURE = 'temperature'
FEED_HUMIDITY = 'humidity'
FEED_PARTICULATE = 'particulate'

# Callback function on connection
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to multiple feeds
    client.subscribe(f"{ADAFRUIT_IO_USERNAME}/feeds/{FEED_TEMPERATURE}")
    client.subscribe(f"{ADAFRUIT_IO_USERNAME}/feeds/{FEED_HUMIDITY}")
    client.subscribe(f"{ADAFRUIT_IO_USERNAME}/feeds/{FEED_PARTICULATE}")

# Callback function on message
def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")

# Setup MQTT client
client = mqtt.Client()
client.username_pw_set(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the loop
client.loop_start()

# Keep the script running to continuously receive messages
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Disconnecting from broker")
    client.loop_stop()
    client.disconnect()
