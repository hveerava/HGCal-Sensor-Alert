import paho.mqtt.client as mqtt

# Adafruit IO credentials
ADAFRUIT_IO_USERNAME = 'jparshook'  # Replace with your Adafruit IO username
ADAFRUIT_IO_KEY = 'aio_pQCI91TyV3iHZovMtPwbRQQ1FELa'  # Replace with your Adafruit IO key

# MQTT broker settings
MQTT_BROKER = 'io.adafruit.com'
MQTT_PORT = 1883

# Feed name
FEED_TEMPERATURE = 'temperature'

# Variable to store the most recent temperature value
latest_temperature = None

# Callback function on connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        print(f"Subscribing to {ADAFRUIT_IO_USERNAME}/feeds/{FEED_TEMPERATURE}")
        # Subscribe to the temperature feed
        client.subscribe(f"{ADAFRUIT_IO_USERNAME}/feeds/{FEED_TEMPERATURE}")
        print("--------1--------Reached here--------1--------")
    else:
        print(f"Connection failed with result code {rc}. Check your username and AIO key.")

# Callback function on message
def on_message(client, userdata, msg):
    print("Message received")
    global latest_temperature
    
    topic = msg.topic.split('/')[-1]
    payload = msg.payload.decode()
    
    print(f"Received message on topic {msg.topic}: {payload}")
    
    if topic == FEED_TEMPERATURE:
        latest_temperature = payload
        print(f"Latest temperature: {latest_temperature}")
    else:
        print("Message topic is not temperature")

# Setup MQTT client
client = mqtt.Client()
client.username_pw_set(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = on_connect
client.on_message = on_message
print("--------3--------Reached here--------3--------")
# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 5)

# Start the loop
client.loop_start()

# Keep the script running to continuously receive messages
try:
    while True:
        pass
except KeyboardInterrupt:
    print("--------4--------Reached here--------4--------")
    print("Disconnecting from broker")
    client.loop_stop()
    client.disconnect()