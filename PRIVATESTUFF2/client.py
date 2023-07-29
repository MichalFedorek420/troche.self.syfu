import socket as s

HOST = '192.168.0.100'
PORT = 58506
BUFFER = 1024
client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST, PORT))

name = input('Twoje imie: ').encode('utf8')

client_socket.send(name)

print(client_socket.recv(BUFFER).decode("utf8"))
