import serial
import time
import queue

pile = []


def func(inst):
    try:
        ser = serial.Serial('/dev/ttyUSB0', baudrate=19200, timeout=10.0)
        pile.append(inst)
        ser.write(b'D+090F')
        return "message envoyé"
    except serial.SerialException:
        return "Impossible de se connecter"
