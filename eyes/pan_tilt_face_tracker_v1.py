# Untitled - By: emeliadaro - Wed Apr 19 2023
#adaped from example on digikey.com by ShawnHymel
from pyb import Pin, Timer
import sensor, image, ustruct
import time
from machine import I2C
from vl53l1x import VL53L1X

#initialize TOF sensor
tof = VL53L1X(I2C(2))

#initialize USB connection
usb = USB_VCP()

#create PWM class to control servos from Nicla Board PWM
class PWM():
    def __init__(self, pin, tim, ch):
        self.pin = pin
        self.tim = tim
        self.ch = ch;


# Some initial settings
threshold_x = 20        # Num pixels BB center x can be from CENTER_X
threshold_y = 20        # Num pixels BB center y can be from CENTER_Y
dir_x = -1               # Direction of servo movement (1 or -1)
dir_y = 1              # Direction of servo movement (1 or -1)

#pan servo settings
servo_pan_speed=0.8
pulse_pan_min=1000 #needs further claibration but kinda works
pulse_pan_max=3000

#tilt servo settings
servo_tilt_speed=0.8
pulse_tilt_min=3000 #needs further calibration but kinda works
pulse_tilt_max=4000

#initial servo positions set halfway between rannge
servo_pos_x = int(((pulse_pan_max - pulse_pan_min) / 2) + pulse_pan_min)
servo_pos_y = int(((pulse_tilt_max - pulse_tilt_min) / 2) + pulse_tilt_min)

pan_port = PWM('PE11', 1, 2)  # Initialize PWM for pan servo
tilt_port = PWM('PE14', 1, 4)  # initialize PWM for tilt servo

#function to send a pulse width to specified servo
def send_pulse(port, p_width):
    tim = Timer(port.tim, freq=25)  #frequency can be anywhere betweet 25 and 50 according to chris
    ch = tim.channel(port.ch, Timer.PWM, pin=Pin(port.pin), pulse_width=p_width)

# intial config of camera
sensor.reset()
sensor.set_contrast(3)
sensor.set_gainceiling(16)
sensor.set_framesize(sensor.QVGA)
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.

# get center coords of camera image
WIDTH = sensor.width()
HEIGHT = sensor.height()
CENTER_X = int(WIDTH / 2 + 0.5)
CENTER_Y = int(HEIGHT / 2 + 0.5)

# start clock
clock = time.clock()

# Create cascade for finding faces
face_cascade = image.HaarCascade("frontalface", stages=25)

# main loop
while(True):

    # Take timestamp (for calculating FPS)
    clock.tick()

    # Take photo
    img = sensor.snapshot()

    # Find faces in image
    objects = img.find_features(face_cascade, threshold=0.75, scale_factor=1.25)

    # Find largest face in image
    largest_face_size = 0
    largest_face_bb = None
    for r in objects:

        # Find largest bounding box
        face_size = r[2] * r[3]
        if (face_size > largest_face_size):
            largest_face_size = face_size
            largest_face_bb = r

        # Draw bounding boxes around all faces
        img.draw_rectangle(r)

    # Find distance from center of face to center of frame
    if largest_face_bb is not None:

        #indicate loop state for debug
        print('if loop -- face detected')

        # Print out the largest face info
        print("Face:", largest_face_bb)

        # Find x, y of center of largest face in image
        face_x = largest_face_bb[0] + int((largest_face_bb[2]) / 2 + 0.5)
        face_y = largest_face_bb[1] + int((largest_face_bb[3]) / 2 + 0.5)

        # Draw line from center of face to center of frame
        img.draw_line(CENTER_X, CENTER_Y, face_x, face_y)

        # Figure out how far away from center the face is (minus the dead zone)
        diff_x = face_x - CENTER_X
        if abs(diff_x) <= threshold_x:
            diff_x = 0
        diff_y = face_y - CENTER_Y
        if abs(diff_y) <= threshold_y:
            diff_y = 0

        # Calculate the relative position the servos should move to based on distance
        mov_x = dir_x * servo_pan_speed * diff_x
        mov_y = dir_y * servo_tilt_speed * diff_y

        # Adjust camera position left/right and up/down
        servo_pos_x = servo_pos_x + mov_x
        servo_pos_y = servo_pos_y + mov_y

        # Constrain servo positions to range of servos
        servo_pos_x = max(servo_pos_x, pulse_pan_min)
        servo_pos_x = min(servo_pos_x, pulse_pan_max)
        servo_pos_y = max(servo_pos_y, pulse_pan_min)
        servo_pos_y = min(servo_pos_y, pulse_pan_max)

        # Set pan/tilt
        print("Moving to X:", int(servo_pos_x), "Y:", int(servo_pos_y))

        send_pulse(pan_port, int(servo_pos_x))  # Send a 500 us pulse
        time.sleep_ms(10)
        send_pulse(tilt_port, int(servo_pos_y))
        time.sleep_ms(10)


    # If there are no faces, don't do anything
    else:

        print("else loop -- no face detected")
        dist=tof.read()
        cmd = usb.recv(4, timeout=5000)
        if int(dist)>500:
           usb.send(1)
        else:
            usb.send(0)
        if (cmd == b'snap'):
            img = sensor.snapshot().compress()
            usb.send(ustruct.pack("<L", img.size()))
            usb.send(img)

    # Print FPS
    print("FPS:", clock.fps())
