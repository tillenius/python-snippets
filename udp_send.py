import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
message = "Hello, World!"

print( "UDP target IP:", UDP_IP )
print( "UDP target port:", UDP_PORT )
print( "message:", message )

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

data = message.encode('ascii')

sock.sendto(data, (UDP_IP, UDP_PORT))
