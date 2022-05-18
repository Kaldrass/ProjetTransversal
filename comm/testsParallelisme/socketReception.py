"""
Réceptionne les instructions transmises par le serveur web pour les ajouter à la Queue d'instructions
"""
#On recoit des octets on les décode
import socket
import multiprocessing as mp

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),8000))

while True:
    msg = s.resc(1024) # exemple buffer how big is the data qu'on veut receive
    if len(msg) <= 0:
        break
    else:
        print(msg.decode("utf-8"))

