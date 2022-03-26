# import paho.mqtt.client as mqtt
# from random import randrange,uniform
# import time
# 
# mqttBroker = "https://mqtt.eclipseprojects.io/"
# client = mqtt.Client("temp")
# client.connect(mqttBroker)
# 
# while True:
#     randNumber = uniform(20.0, 21.0)
#     client.publish("TEMPERATURE", randNumber)
#     print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
#     time.sleep(1)
    
    
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)
topic = "csc2006/carpark1"
while True:
    randNumber = uniform(50.0, 51.0)
    client.publish(topic, randNumber)
    print("Just published " + str(randNumber) + " to Topic "+topic)
    time.sleep(1)