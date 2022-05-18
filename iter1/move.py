import serial
import time

ser = serial.Serial('/dev/ttyUSB0', baudrate=19200, timeout=10.0)
num = 8


# Pour la distance
def forward():
    ser.write(b'D+10000F')
    var = ser.read(num)
    print(var)
    dist = ser.read(num)  # pas une distance
    print(dist)
    return dist


def backward():
    ser.write(b'D-00200F')
    var = ser.read(num)
    print(var)


def right():
    ser.write(b'R-00090F')
    var = ser.read(num)
    print(var)
    ser.close()


def left():
    ser.write(b'R+00090F')
    var = ser.read(num)
    print(var)
    ser.close()


def read():
    ser.write(b'D+00200F')
    var = ser.read(num)
    print(var)
    for i in range(1000):
        dist = ser.read(num)
        time.sleep(0.01)
        print(dist)
        if dist == 20:
            print("close")
    print("done")
