from socket import *

serverName = 'localhost'
serverPort = 12000 # Port to connect to

clientSocket = socket(AF_INET, SOCK_STREAM) # Create a TCP socket
clientSocket.connect((serverName, serverPort)) # Connect to the server

sentence = input('Enter a lowercase sentence: ') # Get input from the user

clientSocket.send(sentence.encode()) # Send the sentence to the server

modifiedSentence = clientSocket.recv(64).decode() # Receive the modified sentence from the server

print('Received from server:', modifiedSentence) # Print the received sentence

clientSocket.close() # Close the socket connection