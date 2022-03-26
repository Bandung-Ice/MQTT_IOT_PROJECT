import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    # print("Received message: ", str(message.payload.decode("utf-8")) 
    # 	+" on topic "+ message.topic
    # 	+" with QOS "+str(message.qos)+ " retain: "+str(message.retain))
    print("ERROR! "+str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("ErrorSubscriber")
topic = "csc2006/logs"
client.connect(mqttBroker)

client.subscribe(topic)
client.on_message = on_message
client.loop_forever()