import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("carpark1")
client.connect(mqttBroker)
topic = "csc2006/carparks/carpark1"
while True:
    randNumber = uniform(00.0, 100.0)
    client.publish(topic, randNumber)
    print("Just published " + str(randNumber) + " to Topic "+topic)
    time.sleep(3)

