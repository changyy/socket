# http://docs.python.org/library/socket.html
import sys, time

if len(sys.argv) < 3 or sys.argv[1] == 'help' :
	print "TCP Thread Server"
	print "Usage> "+sys.argv[0]+" ip port"
	print "  $ python "+sys.argv[0]+" 127.0.0.1 12345"
	print "  $ python "+sys.argv[0]+" \"\" 12345"
	sys.exit(0)

def handler(client, addr):
	logtime = time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )
	print 'accept:', logtime, addr
	while True:
		data = client.recv( 1024 )
		logtime = time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )
		if not data:
			print '\tdisconnect:', logtime, addr
			break
		print "\t", logtime, addr, "Raw(newline->'\\n'): ["+data.replace('\n','\\n')+"]"

import thread
import socket
fd = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
fd.bind( ( sys.argv[1], int( sys.argv[2] ) ) )
fd.listen( 5 );

while True:
	client, addr = fd.accept()
	thread.start_new_thread( handler, (client, addr) )

