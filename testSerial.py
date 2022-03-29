import serial

with serial.Serial() as ser:
    ser.baudRate = 19200
    ser.port = 'COM1'
    ser.open()
    ser.write(b'hello')  # Message de connection
    read = ser.read(5)
    if read == b'hello':
        print("connection établie")

    def convert():
        n = 4  # On lit les 32 prochains bits reçus
        read = ser.read(n)
        dist = int(read)
        return dist

    def detectWall():
        distLimite = 30  # centimètres
        if convert() < distLimite:
            print("1/2 Demi tour")
            return b'rot18'  # Demi-tour
        else:
            return b'fwd20'  # Avance 20 centimètres

    while True:
        dist = convert()
        message = detectWall(dist)
        ser.write(message)
        print('Instruction transmise')
