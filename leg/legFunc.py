import time
from adafruit_servokit import ServoKit

leg1 = [120 , 120 , 87]
leg2 = [110 , 120 , 107]
leg3 = [70 , 60 , 30] 
leg4 = [70 , 60 , 107]

kit = ServoKit(channels = 16)

kit.servo[0].set_pulse_width_range(600,2400) #Parallax Standard Servo
kit.servo[1].set_pulse_width_range(700,2300) #MG995
kit.servo[2].set_pulse_width_range(550,2450) #High Torque

kit.servo[4].set_pulse_width_range(550,2450) #High Torque
kit.servo[5].set_pulse_width_range(600,2400) #MG96R
kit.servo[6].set_pulse_width_range(550,2450) #High Torque

kit.servo[8].set_pulse_width_range(550,2450) #High Torque
kit.servo[9].set_pulse_width_range(500,2500) #FS5106B
kit.servo[10].set_pulse_width_range(500,2450) #High Torque

kit.servo[12].set_pulse_width_range(500,2500) #FS5106B
kit.servo[13].set_pulse_width_range(500,2500) #FS5106B
kit.servo[14].set_pulse_width_range(500,2450) #High Torque

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
def step(data,leg,number):
    for n in range(number):
        for index in range(len(data)-1):
            kit.servo[4*(leg-1)].angle = int(float(data[index][0]))
            kit.servo[4*(leg-1)+1].angle = int(float(data[index][1]))
            print('('+data[index][0]+','+data[index][1]+')')
            time.sleep(0.004)

def standing():
    for i in range 3
        kit.servo[0+i].angle = leg1[i]
        kit.servo[4+i].angle = leg2[i]
        kit.servo[8+i].angle = leg3[i]
        kit.servo[12+i].angle = leg4[i]
    
def UpDown():
    for i in range(4):
        for i in range(10): # go up 
            kit.servo[0].angle -= i 
            kit.servo[1].angle += i
            kit.servo[4].angle -= i
            kit.servo[5].angle -= i
            kit.servo[8].angle += i
            kit.servo[9].angle += i
            kit.servo[12].angle += i
            kit.servo[13].angle += i
            
            time.sleep(0.05)

        for i in range(10): # go down 
            kit.servo[0].angle += i
            kit.servo[1].angle -= i
            kit.servo[4].angle += i
            kit.servo[5].angle += i
            kit.servo[8].angle -= i
            kit.servo[9].angle -= i
            kit.servo[12].angle -= i
            kit.servo[13].angle -= i
            
            time.sleep(0.05)
            
def legUp(leg):
    if leg == 1:
        kit.servo[8].angle -= 5
        kit.servo[9].angle -= 45
        kit.servo[10].angle -= 15
    if leg == 2:
        kit.servo[12].angle -= 25
        kit.servo[13].angle -= 40
        kit.servo[14].angle += 20
        
    if leg == 3:
        kit.servo[0].angle += 5
        kit.servo[1].angle += 45
        kit.servo[2].angle -= 15
    if leg == 4:
        kit.servo[4].angle += 15
        kit.servo[5].angle += 40
        kit.servo[6].angle += 15
    
def legDown(leg):
        if leg == 1:
            kit.servo[8].angle += 5
            kit.servo[9].angle += 45
            kit.servo[10].angle += 15
    