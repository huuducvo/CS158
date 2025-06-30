from socket import *
import threading

serverName = 'localhost'
serverPort = 12000

def send_message():
    clientSocket = socket(AF_INET, SOCK_STREAM) # Create a TCP socket
    clientSocket.connect((serverName, serverPort)) # Connect to the server

    print("Connected to server at", serverName, "on port", serverPort)

    print("Type your message (type 'exit' to quit):")
    while True:
        sentence = input()
        if sentence == 'exit':
            break
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024).decode()
        print("From Server:", modifiedSentence)
    clientSocket.close()

while True:
    send_message()