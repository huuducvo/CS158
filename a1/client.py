from socket import *

serverName = 'localhost'  # Server address
serverPort = 12000  # Port number for the server

#TCP SOCKET_STREAM
clientSocket = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket

clientSocket.connect((serverName, serverPort))  # Connect to the server

sentence = input('Input lowercase sentence: ')  # Get input from the user

length = len(sentence) - 2  # Get the length of the input sentence

clientSocket.send(sentence.encode())  # Send the input sentence to the server

count = 0
data = b''  # Initialize an empty byte string to hold the received data

while count < length:
    data = data + clientSocket.recv(64)  # Receive data in chunks of 64 bytes
    count = len(data)  # Update the count with the length of the received data

data = data.decode()  # Decode the received bytes to a string

print('From Server:', data)  # Print the modified sentence

#Close the socket
clientSocket.close()  # Close the client socket