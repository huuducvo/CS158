from socket import *
import threading

serverName = "localhost"
serverPort = 12000

def receive_messages(clientSocket): # Function to receive messages from the server
    while True:
        try:
            message = clientSocket.recv(1024).decode()
            if message:
                print(message)
            else:
                break
        except:
            break
def send_messages(clientSocket):
    while True:
        message = input("Enter message: ")
        clientSocket.send(message.encode())
        if message == "exit":
            break

def main():
    clientSocket = socket(AF_INET, SOCK_STREAM) # Create a TCP socket
    clientSocket.connect((serverName, serverPort)) # Connect to the server

    print(f"Connected to server at {serverName}:{serverPort}. Type 'exit' to disconnect.")

    receiveThread = threading.Thread(target=receive_messages, args=(clientSocket,)) # Start a thread to receive messages from the server
    receiveThread.start()

    sendThread = threading.Thread(target=send_messages, args=(clientSocket,)) # Start a thread to send messages to the server
    sendThread.start()

    receiveThread.join() # Wait for the receive thread to finish
    print("Exiting client...")

    clientSocket.close()

