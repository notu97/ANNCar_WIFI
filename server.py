# server.py 
import socket                                         
import time

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = '192.168.43.88'   # IP of the Server here                       

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  
f = open('FileName.type','wb')  # Specify the file type that has to be sent and its name 
# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    print("Receiving")
    l = clientsocket.recv(1024)
    while (l):
        print ("Receiving...")
        f.write(l)
        l = clientsocket.recv(1024)
    f.close()
    print("Done....")
    print("Got a connection from %s" % str(addr))
    
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
