from socket import *

serverName = ''
serverPort = 9999
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(4)
print("Server is ready")
while(1):
    connectionSocket, addr = serverSocket.accept()
    query = connectionSocket.recv(1024).decode()
    if(exec(query) != 0):
        response = "True"
    else:
        response = "False"
    connectionSocket.send(response.encode())
    connectionSocket.close()

serverSocket.close()
