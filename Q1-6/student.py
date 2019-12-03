# Import socket module 
import socket			 
import random
import time

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
localhost = socket.gethostname()
listenPort = 3310				

# connect to the server on local computer 
s.connect((localhost, listenPort)) 

# sending message to server
s.send('1155079446')
# create a TCP socket s_2 at port ddddd
port_2 = s.recv(5)
s_2 = socket.socket()
s_2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_2.bind((localhost, int(port_2)))
s_2.listen(5)


# Establish connection with robot. 
r, addr = s_2.accept()	 
print 'Got connection from', addr 
data=r.recv(15)
data.split(",")
port_3, remain = data.split(",")
port_return, surplus = remain.split(".")
print port_3, port_return
r.close() 
# send a thank you message to the robot. 
#r.send('Thank you for connecting at s_2') 
	
# Close the connection with the robot 
	
s_3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s_3.bind((localhost, int(port_3)))
num = random.randrange(6,11)
s_3.sendto(str(num),(localhost,int(port_3)))

s_4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_4.bind((localhost, int(port_return)))
r2, addr2 = s_4.recvfrom(num*10)
print s_4.recv(num*10)
# receive data from the server 
#print s.recv(1024) 
for i in range(0,5):
    s_4.sendto(r2,(localhost,int(port_3)))
    time.sleep(1)

# close the connection 
s.close()	 
