from socket import *


serverPort = 12000 # Port number for the server

serverSocket = socket(AF_INET, SOCK_STREAM) # Create a TCP socket

serverSocket.bind(('', serverPort)) # Bind the socket to the port
# This empty string means the server will accept connections on any available interface

serverSocket.listen(1) # Listen for incoming connections

while True:  # Keep the server running indefinitely

    # accept
    cnSocket, addr = serverSocket.accept()  # Accept a connection from a client
    print('Connection from:', addr)  # Print the address of the connected client

    #receive
    length = cnSocket.recv(2) # Receive the length of the message

    count = 0
    data = b''

    while count < length:
        data = data + cnSocket.recv(64)
        count = len(data)

    #sentence = cSocket.recv(64).decode()  # Receive a large message from the client

    data = data.decode()  # Decode the received bytes to a string

    #process
    capSentence = data.upper()  # Convert the sentence to uppercase

    #send
    cnSocket.send(capSentence.encode())  # Send the modified sentence back to the client

    #close
    cnSocket.close()  # Close the connection with the client
    serverSocket.close()  # Close the server socket
