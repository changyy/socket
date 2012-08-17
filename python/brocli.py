# http://wiki.python.org/moin/UdpCommunication
import socket, sys, select
if len(sys.argv) == 2 and sys.argv[1] == 'help':
	print "Broadcast Client"
	print "Usage> "+sys.argv[0]+" port message"
	print "  $ python "+sys.argv[0]+" 12345 hello"
	print "  $ python "+sys.argv[0]+" 12345 \"hello world\""
	print "  $ python "+sys.argv[0]+" 5602 \"get_info\"  (default)"
	sys.exit(0)
message = sys.argv[2] if len(sys.argv) > 2 else 'get_info'
dest = ( '<broadcast>', int( sys.argv[1] ) ) if len(sys.argv) > 2 else ( '<broadcast>' , 5602 )
fd = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
fd.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
fd.sendto( message, dest )
fd.setblocking(0)

bufferSize = 1024
while True:
	result = select.select([fd],[],[])
	msg = result[0][0].recv(bufferSize) 
	#if result[0][0] <> None:
	#	print result[0][0].getpeername()
	print msg
