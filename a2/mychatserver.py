from socket import *
import threading

serverPort = 12000  # Port number for the server
serverSocket = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket
serverSocket.bind(('', serverPort))  # Bind the socket to the port
# This empty string means the server will accept connections on any available interface
serverSocket.listen(5)  # Listen for incoming connections

# Function to handle client connections
def handle_client(cnSocket, addr):
    print('Connected to:', addr)  # Print the address of the connected client
    
    # Receive
    sentence = cnSocket.recv(1024).decode()  # Decode the received bytes to a string

    # Process
    capSentence = sentence.upper()  # Convert the sentence to uppercase

    # Send
    cnSocket.send(capSentence.encode())  # Send the modified sentence back to the client

    # Close
    cnSocket.close()  # Close the connection with the client

while True:  # Keep the server running indefinitely
    cnSocket, addr = serverSocket.accept()  # Accept a connection from a client
    client_thread = threading.Thread(target=handle_client, args=(cnSocket, addr))
    client_thread.start()
