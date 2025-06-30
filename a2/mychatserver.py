from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

serverSocket.listen(1)
cnSocket, addr = serverSocket.accept()
print("Connection established with:", addr)
sentence = cnSocket.recv(64).decode()
print("Received from client:", sentence)
response = sentence.upper()
cnSocket.send(response.encode())
print("Sent to client:", response)
cnSocket.close()




