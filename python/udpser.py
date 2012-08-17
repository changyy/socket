import socket
import sys

if len(sys.argv) < 3 or sys.argv[1] == 'help':
	print "UDP Receive Server"
	print "Usage> "+sys.argv[0]+" ip port"
	print "  $ python "+sys.argv[0]+" \"\" 12345"
	print "  $ python "+sys.argv[0]+" 127.0.0.1 12345"
	sys.exit(0)

socket_fd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_fd.bind((sys.argv[1],int(sys.argv[2])))

while True:
	data, addr = socket_fd.recvfrom(1024)
	print data.strip(), addr
