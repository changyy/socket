# http://docs.python.org/library/socket.html
import socket, sys
if len(sys.argv) < 4 or sys.argv[1] == 'help':
	print "TCP Send Client"
	print "Usage> "+sys.argv[0]+" ip port message"
	print "  $ python "+sys.argv[0]+" 127.0.0.1 12345 hello"
	print "  $ python "+sys.argv[0]+" 127.0.0.1 12345 \"hello world\""
	sys.exit(0)
fd = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
fd.connect( ( sys.argv[1], int( sys.argv[2] ) ) )
fd.send( sys.argv[3] )
fd.close()
