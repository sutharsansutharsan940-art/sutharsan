import socket
hostname=socket.gethostname()
ip_address=socket.gethostbyname(hostname)
print("your computer name:",hostname)
print("your ip address:",ip_address)
