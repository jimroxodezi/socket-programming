import socket

SERVER_NAME =  "localhost"
SERVER_PORT = 1234
BUFFER_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_NAME, SERVER_PORT))

message = input("Enter your message: ")

#no need to include message is going to since
#connection have already been established.
client.send(message.encode())
client_message = client.recv(BUFFER_SIZE)
print("Message from server: ", client_message.decode())
client.close()