import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)
armData = open('legData.csv','r')
contents = armData.read()
lines = contents.split('\n')
data = []

for line in lines:
    values = line.split(',')
    data.append(values)
armData.close()
data.pop(0)

kit.servo[0].angle = int(float(data[0][0]))+90
kit.servo[1].angle = int(float(data[1][1]))
time.sleep(2)

for index in range(len(data)-1):
    kit.servo[0].angle = int(float(data[index][0]))+90
    kit.servo[1].angle = int(float(data[index][1]))
    print('('+data[index][0]+','+data[index][1]+')')
    time.sleep(0.1)
