# IERG3310 Project

import socket
import random
import time

robotVersion = "3.0";
listenPort = 3310;
socket.setdefaulttimeout(20)
localhost = socket.gethostname()
print "----------------------------------------------------------------------"
print "ROBOT IS STARTED"
print "Robot version " + robotVersion + " started"
print "You are reminded to check for the latest available version"

print ""


# Create a TCP socket to listen connection
print "Creating TCP socket..."
listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listenSocket.bind((localhost, listenPort))
listenSocket.listen(5)
print "Done"

print "\nTCP socket created, ready for listening and accepting connection..."
#print "Waiting for connection on port %(listenPort)s" % locals()
print "Waiting for connection on port", listenPort

# accept connections from outside, a new socket is constructed
s1, address = listenSocket.accept()
studentIP = address[0]
print "\nClient from %s at port %d connected" %(studentIP,address[1])
# Close the listen socket
# Usually you can use a loop to accept new connections
listenSocket.close()

data = s1.recv(10)
print "Student ID received: " + data

iTCPPort2Connect = random.randint(0,9999) + 20000
print "Requesting STUDENT to accept TCP <%d>..." %iTCPPort2Connect

s1.send(str(iTCPPort2Connect))
print "Done"
print "----------------------------------------------------------------------"
time.sleep(1)
print "\nConnecting to the STUDENT s1 <%d>..." %iTCPPort2Connect

now = time.time()
time_count = now +30
while (now<time_count):

	# Connect to the server (student s2)
	s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s2.connect((localhost, iTCPPort2Connect)) 
	print "Connection succeed"

	# Receiving the buffer size from student
	heading = s2.recv(2)
	receive_data = s2.recv(1)
	adding = receive_data[len(receive_data)-1]
	while adding != '*':
		receive_data += s2.recv(1)
		adding = receive_data[len(receive_data)-1]
	receive_buffer_size = receive_data[0:len(receive_data)-1]
	print receive_buffer_size


	messageToTransmit = ""
	for i in xrange(0, 30):
		messageToTransmit += str(random.randint(0,9))
	#for i in xrange(0,int(x) * 2):
	 #   messageToTransmit += str(random.randint(0,9999)).zfill(5)
	print "Message to transmit: " + messageToTransmit
	timeout = time.time() + 1
	while True:
	    s2.sendall(messageToTransmit)
	    if time.time() > timeout:
	        break
	           # s2.sendall(messageToTransmit)
	#for i in xrange(0,5):
	 #   s3.sendto(messageToTransmit,(studentIP,iUDPPortStudent))
	  #  time.sleep(1)
	   # print "UDP packet %d sent" %(i+1)


	s2.close()
	print "----------------------------------------------------------------------"
