import socket

s = socket.socket()
print("Socket is created")

port =  10004            #12233 is the start

s.bind(('',port))
print("socket binded to %s" %(port))

#put socket int listening mode
s.listen(5)    #5 connections can be kept on waiting if the server is busy
                # and anyfarther connections is refused
print("socket is listening")                


while True:
#Establish a connetction with client.
    client, addr = s.accept()
    print("Got connection from", addr)
    msg=""
    while True:
        #receive data from client
        msg = client.recv(1024)
        print('from Client:  '+msg.decode("utf-8"))
        if msg.decode("utf-8")=="CLOSE SOCKET":
            print("connection with ",addr,"has been shut")
            client.close()
            break
           
        capMsg=msg.upper()
        print("responding:        ",capMsg)
        client.send(capMsg)
