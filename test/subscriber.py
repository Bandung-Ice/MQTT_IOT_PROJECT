import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    # print("Received message: ", str(message.payload.decode("utf-8")) 
    # 	+" on topic "+ message.topic
    # 	+" with QOS "+str(message.qos)+ " retain: "+str(message.retain))
    temp = round(float(message.payload.decode("utf-8")),3)
    if(temp>80):
    	errorLog = "Temp :"+str(temp)+ " from:"+message.topic
    	client.publish("csc2006/logs",errorLog)
    print("Received message:", str(temp)) 

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("subscriber1")
topic = "csc2006/carparks/#"
client.connect(mqttBroker)
print("Subscriber Start")
# client.loop_start()
# client.subscribe(topic)
# client.on_message = on_message
# time.sleep(100)
# client.loop_end()

client.subscribe(topic)
client.on_message = on_message
client.loop_forever()