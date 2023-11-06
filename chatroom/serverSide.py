# socket programming for chatrooms, multiplayer games or etc
# client server chat room (server is now localhost)
#individual thread for each client
from threading import Thread
import socket

# creating a socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",5555)) #takes ip and port no. (server is localhost for now)


server.listen() #it takes num of connection to listen (no num given so multiple connections available)

allclients = {}


# function to create a individual thread to client
def client_thread(client):      #takes args as client

    while True:

        try:
            # msg sent by client will be first recieved here
            msg = client.recv(1024)     #not decoding as we've o sent it in byte only

            # now sending msg to allclients
            for c in allclients:
                c.send(msg)
        except:
            # now sending msg to allclients when client left
            for c in allclients:
                if c != client:
                    c.send(f"{name} left the chat".encode())

            del allclients[client]
            client.close()
            break

# to continuesly receive data in real time
while True:

    try:
        print("waiting for connection.....")

        # after listening/accepting request, it returns a tuple
        client, address = server.accept()
        print("connection established.....")

        # to receive any data from client and making different space for individual client
        name = client.recv(1024).decode()   #take size of msg in bytes and then decoded back in string
        print(name)
        
        # appending client name to dictionary
        allclients[client] = name

        # now sending msg to allclients when new client joins
        for c in allclients:
            if c != client:
                c.send(f"{name} joined the chat".encode())

        # creating thread for client by calling func as args and passing an arg
        thread = Thread(target=client_thread, args=(client,))
        # starting a thread
        thread.start()
    except:

        print("something went wrong!...")
        # closing the connection
        client.close()
        break

