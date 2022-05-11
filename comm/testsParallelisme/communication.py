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