# client.py  
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = '192.168.159.154'  # IP of the Server here                         

port = 9999

# connection to hostname on the port.
s.connect((host, port))
f=open('FileNameToSend.type','rb')   #write the file name here in any format(has to be same as received file) 
print("Sending")
l = f.read(1024)
# Receive no more than 1024 bytes
#tm = s.recv(1024)                                     
while (l):
    print ("Sending...")
    s.send(l)
    l = f.read(1024)
f.close()
print("DOne sending")
s.shutdown(socket.SHUT_WR)
print (s.recv(1024))
s.close()

