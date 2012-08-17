# http://docs.python.org/library/socket.html
import socket, sys, time

if len(sys.argv) < 3 or sys.argv[2] == 'help' :
	print "TCP Receive Server"
	print "Usage> "+sys.argv[0]+" ip port"
	print "  $ python "+sys.argv[0]+" 127.0.0.1 12345"
	print "  $ python "+sys.argv[0]+" \"\" 12345"
	sys.exit(0)
fd = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
fd.bind( ( sys.argv[1], int( sys.argv[2] ) ) )
fd.listen( 5 );

while True:
	client, addr = fd.accept()
	data = client.recv( 1024 )
	logtime = time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )
	cmds = data.strip().split( ' ' ) # Length, Action, ActionType, Data
	print logtime, addr
	print "\t", "Raw(newline->'\\n'): ["+data.replace('\n','\\n')+"]"
	client.close()
