import socket as s

server_socket = s.socket(s.AF_INET,s.SOCK_STREAM)
# s.AF_INET to rodzina adresów IPV4
# Strumień przesyłu danych dla socketa
HOST = '192.168.0.100'
PORT = 58506
BUFFER = 1024

server_socket.bind((HOST, PORT))
server_socket.listen(2)

while True:
    client_socket, adress = server_socket.accept()
    print(f"Uzyskano połączenie od {adress}")
    name = client_socket.recv(BUFFER).decode('utf8')
    print(f'[{adress[0]}:{adress[1]}]> Nazwa uzytkownika {name}')
    msg = f'Witaj na serwerze, {name}!'.encode('utf8')
    client_socket.send(msg)