import socket,uuid,platform


print("hostname:",socket.gethostname())
print("local ip:",socket.gethostbyname(socket.gethostname()))
print("platform:",platform.system(),platform.release())
print("mac address:",':'.join(['{:02x}'.format((uuid.getnode()>>elements)&0xff)
                               for elements in range (0,8*6,8)][::-1]))
