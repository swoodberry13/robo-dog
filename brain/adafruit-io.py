from Adafruit_IO import Client, Feed, Data, RequestError
import datetime
import time
import serial
import requests
import time
import numpy as np
from PIL import Image
import base64
import json


        
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_gjuJ031DNgzdCo5PKqIa6F3H6YFW'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'aayushma'


aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
digital = aio.feeds('legooo')
image = aio.feeds('pic')
servo_feeds = []
s0 = aio.feeds('robotdog.s0')
s1 = aio.feeds('robotdog.s1')
s4 = aio.feeds('robotdog.s4')
s5 = aio.feeds('robotdog.s5')
s8 = aio.feeds('robotdog.s8')
s9 = aio.feeds('robotdog.s9')
s12 = aio.feeds('robotdog.s12')
s13 = aio.feeds('robotdog.s13')



    
# try:
#     temperature = aio.feeds('midterm')
# except RequestError:
#     feed = Feed(name="LEGOooo")
#     temperature = aio.create_feed(feed)

def image_send():

    BASE_DIR='/Users/ngimahyolmo/Desktop/'
    SRC_FILE=BASE_DIR+'image.jpg'
    DST_FILE=BASE_DIR+'lastsmall.jpg'

    fd_img = open(SRC_FILE, 'rb')
    img = Image.open(fd_img)
    size = 320,240
    img.thumbnail(size)
    img.save(DST_FILE, img.format)
    fd_img.close()

     
    with open(DST_FILE, 'rb') as image_file:
        str1= base64.b64encode(image_file.read())
        aio.send('pic',str1.decode() )
        print('pic_sent')

  


def run():
    
        pass
    #add leg code here
    
    
timer = 0
leg1 = [110 , 130 ]
leg2 = [110 , 130 ]
leg3 = [80 , 40 ] 
leg4 = [70 , 40 ]
while True:
   
    data = aio.receive(digital.key)
    if (data.value) == "ON":
        run()
    elif (data.value) == "OFF":
        print('received <- OFF\n')
    timer+=1
    time.sleep(0.4)
    if(timer%10==0):
        image_send()
        
        aio.send(s0.key,leg1[0] )
        aio.send(s1.key,leg1[1] )
        aio.send(s4.key,leg2[0] )
        aio.send(s5.key,leg2[1] )
        aio.send(s8.key,leg3[0] )
        aio.send(s9.key,leg3[1] )
        aio.send(s12.key,leg4[0] )
        aio.send(s13.key,leg4[1] )

            







