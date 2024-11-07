import socket
import os
import time
import json

os.system("clear")

ip = input("IP du serveur de jeu: ")
port = input("Quel code de connexion du serveur de jeu: ")
port = int(port)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))
print(f"Connexion réussi sur le serveur de jeu {ip}")

while True:
    data = sock.recv(1024)
    diff_coordonnées = json.loads(data.decode('utf-8'))

    print(diff_coordonnées["aa"], diff_coordonnées["ab"], diff_coordonnées["ac"], end='\n')
    print(diff_coordonnées["ba"], diff_coordonnées["bb"], diff_coordonnées["bc"], end='\n')
    print(diff_coordonnées["ca"], diff_coordonnées["cb"], diff_coordonnées["cc"], end='\n\n')

    while True:
        coordonnée = input(str("Quelle coordonnée voulez-vous jouer: "))
        if coordonnée in diff_coordonnées and diff_coordonnées[coordonnée] == "-":
            diff_coordonnées[coordonnée] = "X"
            break
        else:
            print("Mauvaise coordonnée")
            pass

    grille_json = json.dumps(diff_coordonnées)

    sock.sendall(grille_json.encode('utf-8'))

    print(diff_coordonnées["aa"], diff_coordonnées["ab"], diff_coordonnées["ac"], end='\n')
    print(diff_coordonnées["ba"], diff_coordonnées["bb"], diff_coordonnées["bc"], end='\n')
    print(diff_coordonnées["ca"], diff_coordonnées["cb"], diff_coordonnées["cc"], end='\n\n')


