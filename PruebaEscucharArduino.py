# Echo server program
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.0.6', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    print >>sys.stderr, 'connection from', client_address
    data = connection.recv(64)
        #print(data)
    print >>sys.stderr, 'data received ', data
	
    data2 = data.decode('utf-8')
    string2 = "2c10c20c30c40"
    print >>sys.stderr, 'data received ', data
    connection.close()

    if data2[0] == "2":
        connection, client_address = sock.accept()
        #print('waiting for a connection 2 ', client_address)
        print >>sys.stderr, 'waiting for a connection 2 ', client_address
        print >>sys.stderr, 'sending data back to the client'
        c = string2
        connection.send(c.encode('utf-8'))
        connection.close()