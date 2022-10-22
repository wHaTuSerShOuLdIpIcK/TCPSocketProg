import socket
import threading

HOST = '127.0.0.1'
PORT = 9091

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
print ("server Socket successfully created")
server.bind((HOST, PORT))        
print ("socket bound to %s" %(PORT))

server.listen()    
print ("server socket is listening")

clients = []
nickname = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client, address):
    while True:
        try:
            message = client.recv(1024)
            print(f"Client {str(address)} says {message.decode('utf-8')}")
            broadcast(message.decode("utf-8").upper())
            if message.decode("utf-8")=="CLOSE SOCKET":
                print("connection with ",address,"has been shut")
                client.close()
                break
        except:
            clients.remove(client)
            print(f"Client {address} disconnected")
            client.close()
            pass

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")
        clients.append(client)
        broadcast(f"Client {address} connected to the server".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client, address))
        thread.start()

print("Server running...")

receive()