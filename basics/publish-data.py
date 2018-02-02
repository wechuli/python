import paho.mqtt.client as mqtt
import json
# Define Variables
MQTT_HOST = "54.224.229.75"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "feeds"

MQTT_MSG=json.dumps({"current":  "30","longitude": "-3.2588","oil_level":  "1.5","tracker_id": "85", "latitude": "-3.2588", "temperature": "23.01"})
# Define on_publish event function
def on_publish(client, userdata, mid):
    print ("Message Published...")

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC)
    client.publish(MQTT_TOPIC, MQTT_MSG)

def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload) # <- do you mean this payload = {...} ?
    payload = json.loads(msg.payload) # you can use json.loads to convert string to json
    print(payload['oil_level']) # then you can check the value
    client.disconnect() # Got message then disconnect
def message():
    print("Lets see what happens")
m=message()
print(m)
# Initiate MQTT Client
mqttc = mqtt.Client()

# Register publish callback function
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect
mqttc.on_message = on_message

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# Loop forever
mqttc.loop_forever()