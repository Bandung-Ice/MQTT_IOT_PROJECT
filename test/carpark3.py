# import paho.mqtt.client as mqtt
# from random import randrange, uniform
# import time

# mqttBroker = "mqtt.eclipseprojects.io"
# client = mqtt.Client("carpark2")
# client.connect(mqttBroker)
# topic = "csc2006/carpark2"
# while True:
#     randNumber = uniform(20.0, 21.0)
#     client.publish(topic, randNumber)
#     print("Just published " + str(randNumber) + " to Topic "+topic)
#     time.sleep(1)

import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("carpark3")
client.connect(mqttBroker)
topic = "csc2006/carparks/carpark3"
while True:
    randNumber = uniform(0, 100)
    client.publish(topic, randNumber)
    print("Just published " + str(randNumber) + " to Topic "+topic)
    time.sleep(3)
