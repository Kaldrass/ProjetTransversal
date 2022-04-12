import serial

def func():
    try:
        with serial.Serial() as ser:
            ser.baudRate = 19200
            ser.port = 'COM1'
            ser.open()
            ser.write(b'D+020F')
            print("Message envoyé!")
            return "message envoyé!"
    except serial.SerialException:
        print("Erreur connexion")
        return "Impossible de se connecter au port COM1"
        