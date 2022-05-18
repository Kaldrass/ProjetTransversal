"""
Gestionnaires de communication
- STM32 :
    Lecture et écriture en alternance
    Lecture :
        Par paquet de 8 octets jusqu'à recevoir un octet contenant l'information de fin de transmission
    Écriture :
        Comme établi avant (rotation / translation + sens + valeur) à partir de la seconde queue
- LIDAR :
    Réception uniquement
- Caméra
Envoi des données dans la Queue avec Header indiquant le type de capteur
"""
import serial


def comStm(sem, q, q2):
    with serial.Serial('/dev/ttyUSB0', baudrate=19200, timeout=10.0) as ser:
        while True:
            with sem.acquire():
                ser.write(q2.get())  # Déjà en binaire ?
            data = []
            while True:
                read = ser.read(1)
                data.append(read)
                if read == b'F':
                    if len(data) != 8:
                        raise Exception("Erreur message incomplet")  # TODO gérer exception
                    break
            q.put(data)
            '''
            Attention à ajouter quand l'instruction est dispo dans la q2
            if data[0] == b'S':  # S pour statut e.g (fini instruction, fini mais pb, ..)
                sem.release()
            '''


def comLidar():
    # Comment ?
    pass


def comCamera():
    # Réception image et envoyer des frames
    pass
