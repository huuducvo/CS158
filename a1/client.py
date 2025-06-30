from socket import *

serverName = 'localhost'  # Server address
serverPort = 12000  # Port number for the server

#TCP SOCKET_STREAM
clientSocket = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket

clientSocket.connect((serverName, serverPort))  # Connect to the server

sentence = input('Input lowercase sentence: ')  # Get input from the user

clientSocket.send(sentence.encode())  # Send the input sentence to the server

modifiedSentence = clientSocket.recv(64)  # Receive the modified sentence from the server

print('From Server:', modifiedSentence.decode())  # Print the modified sentence

#Close the socket
clientSocket.close()  # Close the client socket