from socket import *
import struct

serverPort = 12000 # Port number for the server

serverSocket = socket(AF_INET, SOCK_STREAM) # Create a TCP socket

serverSocket.bind(('', serverPort)) # Bind the socket to the port
# This empty string means the server will accept connections on any available interface

serverSocket.listen(1) # Listen for incoming connections

while True:  # Keep the server running indefinitely


    def receive_large_message(sock, buffer_size=4096):
        # Receive a large message from the client
        len_bytes = sock.recv(2)
        if not len_bytes:
            return None # Client does not send any length bytes, return None
        
        message_length = struct.unpack('>I', len_bytes)[0]  # Unpack the length of the message
        receive_data = b''  # Initialize an empty byte string to hold the received data
        bytes_received = 0 # Initialize the number of bytes received

        while bytes_received < message_length:
            # Continue receiving data until the entire message is received
            remaining_bytes = message_length - bytes_received
            chunk_size = min(buffer_size, remaining_bytes)
            chunk = sock.recv(chunk_size)
            if not chunk:
                break   # No more data, break the loop
            receive_data += chunk
            bytes_received += len(chunk)
        return receive_data.decode()

    # accept
    cSocket, addr = serverSocket.accept()  # Accept a connection from a client
    print('Connection from:', addr)  # Print the address of the connected client

    #receive
    sentence = receive_large_message(cSocket)  # Receive a large message from the client

    #process
    modifiedSentence = sentence.upper()  # Convert the sentence to uppercase
    print(modifiedSentence)
    modifiedSentence = f"{len(modifiedSentence):>2}{modifiedSentence}"  # Prepend the length of the modified sentence
    print(modifiedSentence)

    #send
    cSocket.send(modifiedSentence.encode())  # Send the modified sentence back to the client

    #close
    cSocket.close()  # Close the connection with the client
