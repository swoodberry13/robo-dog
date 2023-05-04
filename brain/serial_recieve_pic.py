import serial
import struct
# open the serial port
ser = serial.Serial(‘/dev/ttyACM0’, 115200)
ser.write(b”snap”)
# receive the size of the image over serial
size = struct.unpack(‘<L’, ser.read(4))[0]
# receive the image over serial
img = ser.read(size)
# save the image to disk
with open(‘image.jpg’, ‘wb’) as f:
    f.write(img)
# close the serial port
ser.close()
