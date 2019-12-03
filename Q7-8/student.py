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
now = time.time()
time_count = now +30
i=1
# sending message to server
s.send('1155079446')
# create a TCP socket s_2 at port ddddd
port_2 = s.recv(5)
port_in_loop = int (port_2)


total_size=0
total_packet=0
total_time=0
while (now<time_count):
#	various_buffer= (i*50.0/100.0)*1000
	localhost = socket.gethostname()
	listenPort = 3310
	s_2 = socket.socket()
	s_2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s_2.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 2500)
	s_2.bind((localhost, int(port_in_loop)))
	s_2.listen(5)
	

	print "----------------------------------------------------------------------" 
	#Buffersize
	buffer_size = s_2.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
	print i
	print "Existing receiver buffer size: " + str(buffer_size) + " bytes"
	print "\nTCP socket created, ready for connection..."
	print "Waiting for connection on port", listenPort
	r, address = s_2.accept()
	#showing status (optional)
	studentIP = address[0]
	print "\nClient from %s at port %d connected" %(studentIP,address[1])
	###

	s_2.close()
	# * is a notation for the end of the string
	buffer_size_str = "bs" + str(buffer_size) + "*"
	r.send(buffer_size_str)
	print "Buffer size has been sent!!"


	#receiving packet 
	print "Receiving the packets from robot..."
	message =""
	message_b = r.recv(buffer_size)
	message += message_b
	count = 0
	now = time.time()
	while message_b:
		message += r.recv(buffer_size)
		message_b = r.recv(buffer_size)
		count +=1
		r_time = time.time() - now
	total_size+= len(message)
	total_packet+= count
	total_time+= r_time
	print "Size: " + str(len(message)) + "bytes"
	print "Packets: " + str(count)
	print "Time: " + str(r_time)
	print "System throughput: " , len(message)/r_time
	print "Number of received packets: " +str(count) +",total received bytes: " + str(len(message)) + "bytes"

	r.close()
	i=i+1
	print "----------------------------------------------------------------------" 
print "Total size: " + str(total_size) + "bytes"
print "Total packet: " + str(total_packet)
print "Total time: " + str(total_time)
