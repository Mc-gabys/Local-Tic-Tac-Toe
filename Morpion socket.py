import socket
import os
import time
import json

os.system("clear")

host = '0.0.0.0'
port = input("Quel code de connexion: ")
port = int(port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)
sock.settimeout(0.5)

connected = False

titre = "L'adresse IP de connexion: "+[ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0]+ f" code de connexion: {port}"
os.system(f'echo -n "\033]0;{titre}\007"')

while not connected:
    for i in range(4):
        os.system("clear")
        print(f"Serveur en attente de connexion sur le port {port}{'.' * i}")
        time.sleep(0.5)
        
        try:
            client_socket, client_address = sock.accept()
            connected = True 
            break
        except socket.timeout:
            pass

if connected:
    os.system("clear")
    print(f"\rConnexion établie avec {client_address}")

diff_coordonnées = {
    "aa": '-', "ab": '-', "ac": '-',
    "ba": '-', "bb": '-', "bc": '-',
    "ca": '-', "cb": '-', "cc": '-'
}

while True:
    print(diff_coordonnées["aa"], diff_coordonnées["ab"], diff_coordonnées["ac"], end='\n')
    print(diff_coordonnées["ba"], diff_coordonnées["bb"], diff_coordonnées["bc"], end='\n')
    print(diff_coordonnées["ca"], diff_coordonnées["cb"], diff_coordonnées["cc"], end='\n\n')

    while True:
        coordonnée = input(str("Quelle coordonnée voulez-vous jouer: "))
        if coordonnée in diff_coordonnées and diff_coordonnées[coordonnée] == "-":
            diff_coordonnées[coordonnée] = "O"
            break
        else:
            print("Mauvaise coordonnée")
            pass

    grille_json = json.dumps(diff_coordonnées)

    client_socket.sendall(grille_json.encode('utf-8'))

    print(diff_coordonnées["aa"], diff_coordonnées["ab"], diff_coordonnées["ac"], end='\n')
    print(diff_coordonnées["ba"], diff_coordonnées["bb"], diff_coordonnées["bc"], end='\n')
    print(diff_coordonnées["ca"], diff_coordonnées["cb"], diff_coordonnées["cc"], end='\n\n')
    
    data = client_socket.recv(1024)
    diff_coordonnées = json.loads(data.decode('utf-8'))

