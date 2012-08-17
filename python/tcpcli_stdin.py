# http://docs.python.org/library/socket.html
import socket, sys
if len(sys.argv) < 3 or sys.argv[1] == 'help':
	print "TCP Client"
	print "Usage> "+sys.argv[0]+" ip port"
	print "  $ python "+sys.argv[0]+" 127.0.0.1 12345"
	sys.exit(0)
fd = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
fd.connect( ( sys.argv[1], int( sys.argv[2] ) ) )
for line in iter(sys.stdin.readline, ""):
	if line.find('quit') != -1:
		break
	fd.send( line )
fd.close()
