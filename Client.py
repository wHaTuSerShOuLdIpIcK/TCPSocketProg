import socket
# Create a socket object
s = socket.socket()

#Define the port on which you want to connet
port = 10004        #12233 is the start

#connect to server on local computer
s.connect(('127.0.0.1',port))

#send data to the server
while True:    
    message = input("Enter your message: ")
    s.send(bytes(message,"utf-8"))
    
    #recieve data from the server
    msg = s.recv(1024)
    
    print("server response:   ",msg.decode("utf-8"))

    if message=="CLOSE SOCKET":
        s.close()
        break;
    