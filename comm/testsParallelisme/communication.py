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