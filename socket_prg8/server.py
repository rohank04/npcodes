from socket import *

serverName = ''
serverPort = 12000
serverSocket = socket(AF_INET6, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(4)
print("Server is ready")
while(1):
    connectionSocket, addr = serverSocket.accept()
    query = connectionSocket.recv(1024).decode()
    file_pointer = open(query, 'r')
    file_content = file_pointer.read(1024)
    connectionSocket.send(file_content.encode())
    connectionSocket.close()

serverSocket.close()
