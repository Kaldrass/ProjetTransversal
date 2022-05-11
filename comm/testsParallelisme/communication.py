"""
Gestionnaires de communication
- STM32 :
    Lecture et écriture en alternance
    Lecture :
        Par paquet de 8 octet jusqu'à recevoir un octet contenant l'information de fin de transmission
    Ecriture :
        Comme établi avant (rotation / translation + sens + valeur) à partir de la seconde queue
- LIDAR :
    Réception uniquement

Envoi des données dans la Queue avec Header indiquant le type de capteur
"""
import threading
import OSC
import threading
import atexit
#------OSC Server-------------------------------------#
receive_address = '192.168.151.24', 8000
exit_flag = 0

# OSC Server. there are three different types of server.
s = OSC.ThreadingOSCServer(receive_address)

# this registers a 'default' handler (for unmatched messages)
s.addDefaultHandlers()
class recieve:
    def printing_handler(self, addr, tags, data, source)


