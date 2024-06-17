import paho.mqtt.client as mqtt

# Adafruit IO credentials
ADAFRUIT_AIO_USERNAME = ""
ADAFRUIT_AIO_KEY      = ""

# MQTT broker settings
MQTT_BROKER = 'io.adafruit.com'
MQTT_PORT = 1883

# Feed names
FEED_TEMPERATURE = 'temperature'
FEED_HUMIDITY = 'humidity'
FEED_PARTICULATE = 'particulate'

# Variables to store the most recent values
latest_temperature = None
latest_humidity = None
latest_particulate = None

# Callback function on connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        # Subscribe to the feeds
        client.subscribe(f"{ADAFRUIT_AIO_USERNAME}/feeds/{FEED_TEMPERATURE}")
        client.subscribe(f"{ADAFRUIT_AIO_USERNAME}/feeds/{FEED_HUMIDITY}")
        client.subscribe(f"{ADAFRUIT_AIO_USERNAME}/feeds/{FEED_PARTICULATE}")
    else:
        print(f"Connection failed with result code {rc}. Check your username and AIO key.")

# Callback function on message
def on_message(client, userdata, msg):
    global latest_temperature, latest_humidity, latest_particulate
    print("heres ur on message")
    '''topic = msg.topic.split('/')[-1]
    payload = msg.payload.decode()
    
    print(f"Received message on topic {msg.topic}: {payload}")

    if topic == FEED_TEMPERATURE:
        latest_temperature = payload
    elif topic == FEED_HUMIDITY:
        latest_humidity = payload
    elif topic == FEED_PARTICULATE:
        latest_particulate = payload

    # Print the entire feed
    print(f"Latest temperature: {latest_temperature}")
    print(f"Latest humidity: {latest_humidity}")
    print(f"Latest particulate: {latest_particulate}")'''

# Setup MQTT client
client = mqtt.Client()
client.username_pw_set(ADAFRUIT_AIO_USERNAME, ADAFRUIT_AIO_KEY)
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
