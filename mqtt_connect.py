import paho.mqtt.client as mqtt

# Adafruit IO credentials


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

# Callback function on publish
def on_publish(client, userdata, mid):
    print("Message published")

# Setup MQTT client
client = mqtt.Client()
client.username_pw_set(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the loop
client.loop_start()

# Publish test messages to each feed
client.publish(f"{ADAFRUIT_IO_USERNAME}/feeds/{FEED_TEMPERATURE}", "23.5")  # Example temperature
client.publish(f"{ADAFRUIT_IO_USERNAME}/feeds/{FEED_HUMIDITY}", "60.2")    # Example humidity
client.publish(f"{ADAFRUIT_IO_USERNAME}/feeds/{FEED_PARTICULATE}", "15")   # Example particulate

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Disconnecting from broker")
    client.loop_stop()
    client.disconnect()

# problem: sensor not sending any data to adafruit dashboard. not reflecting.
# configure raspi and enviro to relay data to dashboard and set alert system