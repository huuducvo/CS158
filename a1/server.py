from socket import *

serverPort = 12000 # Port to listen on

serverSocket = socket(AF_INET, SOCK_STREAM) # Create a TCP socket

serverSocket.bind(('', serverPort)) # Bind the socket to the port
# Listen for all incoming connections

serverSocket.listen(1) # Allow one connection at a time

sentence = ""

while True:
    #Accept
    cnSocket, addr = serverSocket.accept() # Accept a connection
    print('Connected from:', addr) # Print the address of the client

    # Receive
    sentence = cnSocket.recv(64).decode() # Receive the sentence from the client
    length= int(sentence[0:2])
    sentence = sentence[2:2 + length]
    sentencelength =  62

    #Process
    while length >= sentencelength:
        sentence += cnSocket.recv(64).decode() # Receive the sentence from the client
        sentencelength += 64

    print('Received from client:', sentence) # Print the received sentence

    upperSentence = sentence.upper() # Convert the sentence to uppercase

    # Send
    cnSocket.send(upperSentence.encode()) # Send the modified sentence back to the client

    print('Sent to client:', upperSentence) # Print the sent sentence

    # Close
    cnSocket.close() # Close the connection with the client