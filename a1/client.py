from socket import *
serverName = 'localhost'  # Server address
serverPort = 12000  # Port number for the server

#TCP SOCKET_STREAM
clientSocket = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket

clientSocket.connect((serverName, serverPort))  # Connect to the server

sentence = input('Input lowercase sentence: ')  # Get input from the user

clientSocket.send(sentence.encode())  # Send the input sentence to the server

def receive_large_message(sock, buffer_size=4096):
        # Receive a large message from the client
        len_bytes = sock.recv(2)
        if not len_bytes:
            return None # Client does not send any length bytes, return None
        
        message_length = struct.unpack('>I', len_bytes)[0]  # Unpack the length of the message
        receive_data = b''
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

modifiedSentence = receive_large_message(clientSocket)  # Receive the modified sentence from the server

print('From Server:', modifiedSentence)  # Print the modified sentence

#Close the socket
clientSocket.close()  # Close the client socket 