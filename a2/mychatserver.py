from socket import *
import threading

serverName = "localhost" # Server's hostname
serverPort = 12000  # Server's port number

clientList = [] # List of connected clients
lock = threading.Lock() # Lock for synchronizing access to clientList

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM) # Create a TCP socket
    serverSocket.bind((serverName, serverPort)) # Bind the socket to the server address and port
    serverSocket.listen(5) # Listen for incoming connections
    print(f"Server is listening on {serverName}:{serverPort}")

    while True:
        clients, addr = serverSocket.accept() # Accept a new client connection
        print(f"New connection from {addr}")
        clientThread = threading.Thread(target=handle_client, args=(clients, addr))
        clientThread.start() # Start a new thread to handle the client

def handle_client(clients, addr):
    with lock: # Acquire the lock before modifying clientList
        clientList.append(clients)
        print(f"Client {addr} connected. Total clients: {len(clientList)}")

    while True:
        sentence = clients.recv(1024).decode() # Receive message from client

        if sentence == "exit": # Check if the message is "exit"
            print(f"Client {addr} requested to exit.")
            with lock:
                clientList.remove(clients)
                print(f"Client {addr} disconnected. Total clients: {len(clientList)}")
                clients.close()
                break
        else:
            print(f"Received from {addr}: {sentence}")
            with lock:
                for client in clientList: # Broadcast the message to all other clients
                    if client != clients: # Don't send the message back to the sender
                        client.send(f"From {addr}: {sentence}".encode())

