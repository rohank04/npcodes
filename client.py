from socket import *

serverName = '0:0:0:0:0:0:0:1'
serverPort = 12000
clientSocket = socket(AF_INET6, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
query = input("Enter File name : ")
clientSocket.send(query.encode())
filecontent = clientSocket.recv(1024).decode()
print(filecontent)
