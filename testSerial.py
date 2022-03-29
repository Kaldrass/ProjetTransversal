import serial

with serial.Serial() as ser:
    ser.baudRate = 19200
    ser.port = 'COM1'
    ser.open()
    ser.write(b'hello')  # Message de connection
    read = ser.read(5)  #
    if read == b'hello':
        ser.write(b'fwd10')  # Avancer 10 centimètres
