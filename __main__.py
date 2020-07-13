import json
import socket

with open("consts.json") as f:
    json_data = json.load(f)

readbuffer = ""

server = json_data['server']
port = json_data['port']
token = json_data['token']
channel = json_data['channel']
nickname = 'chatchesspollbot'

sock = socket.socket();
sock.connect((server,port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

def sendMessage(message):
    s.send(f"PRIVMSG {channel} :" + message + "\r\n")

while True:
    readbuffer = readbuffer + str(sock.recv(1024))
    temp = str.split(readbuffer, "\\n")
    readbuffer = temp.pop()

    for line in temp:
        if (line[0] == "PING"):
            s.send("PONG %s\r\n" % line[1])
        else:
            parts = str.split(line, ":")
 
            if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                try:
                    message = parts[2][:len(parts[2]) - 1]
                except:
                    message = ""

                usernamesplit = str.split(parts[1], "!")
                username = usernamesplit[0]

                MODT = False

                for l in parts:
                    if "End of /NAMES list" in l:
                        MODT = True
               
                message = message[:-1]

                print("Message: " + str(message))
                if MODT:
                    print(username + ": " + message)
                   
                    # You can add all your plain commands here
                    if message == "Hey":
                        sendMessage("Welcome to my stream, " + username)
 
