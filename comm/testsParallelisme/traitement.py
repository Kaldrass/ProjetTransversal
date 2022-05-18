"""
Démultiplexage pour traiter chaque type de données indépendamment
Traitement données
Utilisation du résultat pour construire et compléter le graph (!) / Pour identifier notre position dans le graphe
Capteurs : roue codeuse, caméra, LIDAR
"""


def demultiplexeur(q):
    # On oriente le block de données vers la fonction associée au capteur
    while True:
        data = q.get()
        if data[0] == 'R':
            inRoueCodeuse(data[1:])
        elif data[0] == 'C':
            inCamera(data[1:])
        elif data[0] == 'L':
            inLidar(data[1:])
        elif data[0] == 'U':
            inUltrason(data[1:])
        elif data[0] == 'S':
            inStatus(data[1:])

        else:
            raise Exception("Capteur inconnu")


def inStatus(data):
    print("ok")


def inRoueCodeuse(data):
    print("ok")


def inCamera(data):
    print("ok")


def inLidar(data):
    print("ok")


def inUltrason(data):
    print("ok")
