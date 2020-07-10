import json
import socket

with open("consts.json") as f:
	json_data = json.load(f)

server = json_data['server']
port = json_data['port']
token = json_data['token']
channel = json_data['channel']
nickname = 'ayushboss23'

sock = socket.socket();
sock.connect((server,port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

resp = sock.recv(2048).decode('utf-8')

resp = sock.recv(2048).decode('utf-8')

print(resp)
