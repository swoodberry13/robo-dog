from adafruit_servokit import ServoKit
import time

leg1 = [110 , 50 , 87]
leg2 = [110 , 130 , 107]
leg3 = [70 , 50 , 5] 
leg4 = [70 , 50 , 117]

kit = ServoKit(channels = 16)

for serv in range(4):
    kit.servo[4*serv].set_pulse_width_range(550,2450)
    kit.servo[4*serv+1].set_pulse_width_range(550,2450)
    
for i in range(5):
    kit.servo[0].angle = leg1[0] + i
    kit.servo[1].angle = leg1[1] - 2*i 
    kit.servo[2].angle = leg1[2] + 2*i
    
    kit.servo[4].angle = leg2[0] + i
    kit.servo[5].angle = leg2[1] + 2*i 
    kit.servo[6].angle = leg2[2] - 2*i

    kit.servo[10].angle = leg3[2] - i

    kit.servo[14].angle = leg3[2] + i
    
    time.sleep(0.05)
    
for i in range(10):
    kit.servo[12].angle = leg3[2] - i
    kit.servo[13].angle = leg3[2] - i
    
    time.sleep(0.05)

