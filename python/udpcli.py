import socket
import sys
if len(sys.argv) < 4 or sys.argv[1] == 'help':
	print "UDP Send Client"
	print "Usage> "+sys.argv[0]+" ip port message"
	print "  $ python "+sys.argv[0]+" 127.0.0.1 12345 hello"
	print "  $ python "+sys.argv[0]+" 127.0.0.1 12345 \"hello world\""
	sys.exit(0)

socket_fd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_fd.sendto(sys.argv[3],(sys.argv[1],int(sys.argv[2])))
#print socket_fd.recvfrom(1024)
