from socket import *

serverName = '127.0.0.1'
serverPort = 9999
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
query = input("Enter cmd: ")
clientSocket.send(query.encode())
if(clientSocket.recv(1024).decode() == "True"):
    print("Success")
else:
    print("Failed")

