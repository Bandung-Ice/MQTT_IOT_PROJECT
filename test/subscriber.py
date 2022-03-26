import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone")
topic = "csc2006/+"
client.connect(mqttBroker)
# 
client.loop_start()
client.subscribe(topic)
client.on_message = on_message
#time.sleep(100)
client.loop_end()
