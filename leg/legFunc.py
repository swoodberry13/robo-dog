import time
from adafruit_servokit import ServoKit

# function to import a CSV file and process it to an array of 1x2 cells, containing two angles: first one is theta1, second is theta2
# filename must be a string and must include .csv
# function returns processed data such that data = importCSV(filename)
def importCSV(filename):
    armData = open(filename,'r')
    contents = armData.read()
    lines = contents.split('\n')
    data = []
    
    for line in lines:
        values = line.split(',')
        data.append(values)
    armData.close()
    data.pop(0)
    return data

# takes the processed data from the function above as the first argument
# function begins by moving leg to initial postion for the step
# then loops through the angles in the data array and moves the leg
# second input number corresponds to how many steps are wanted
def step(data,number):
    kit = ServoKit(channels = 16)
    kit.servo[0].angle = int(float(data[0][0]))+90
    kit.servo[1].angle = int(float(data[0][1]))
    time.sleep(2)
    
    for n in range(number):
        for index in range(len(data)-1):
            kit.servo[0].angle = int(float(data[index][0]))+90
            kit.servo[1].angle = int(float(data[index][1]))
            print('('+data[index][0]+','+data[index][1]+')')
            time.sleep(0.007)
    