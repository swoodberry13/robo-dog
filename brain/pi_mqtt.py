import serial
import requests
import time
import numpy as np
import paho.mqtt.client as mqtt

fred = mqtt.Client('brain')

topic = "dog"

fred.connect('10.245.152.167')

def trackMessage(user, userName, message):
    started=True
    x =  message.payload.decode()
    print("Message: " + x);
    file1 = open("/Users/ngimahyolmo/Desktop/me35/angles.txt", "w")
    text = x
    file1.write(text)
    file1.close()
    
# Subscription
fred.on_message = trackMessage
fred.loop_start()
fred.subscribe(topic)

#send binary message for testing for now
message = 1
while True:
        fred.publish(topic,message )
        # Run the loop for 2 seconds
        time.sleep(1)  
        #fred.loop_stop()
