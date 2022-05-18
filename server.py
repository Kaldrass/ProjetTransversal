import django
import socket
print(django.get_version())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(,8000))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established!")
    clientsocket.send()#mettre ce qu'on veut envoyer au client exemple "blabla",utf-8.
