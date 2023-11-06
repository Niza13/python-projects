import socket
from threading import Thread


# client will enter a name in begining for cretating individual thread and append in client dict
name = input("enter your name:")

# creating a socket for client
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("localhost",5555)) #in client side bind func


# now sending name to server
client.send(name.encode())


# func to send msg
def send(client):
    
    while True: 
        # msg to send to client
        data = f"{name}: {input()}"     #name so one can know which client send the msg
        client.send(data.encode())

# func to receive msg
def receive(client):
    while True:
        try:
            data = client.recv(1024).decode()       #receive data from other clients
            print(data)
        except:

            print("somethong went wrong while receiving...")
            client.close()
            break
        

# creating and starting threads to recieve and send msg 
thread1 = Thread(target=send, args=(client,))
thread1.start()
thread2 = Thread(target=receive, args=(client,))
thread2.start()
        

