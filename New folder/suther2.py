import socket
domain=input("enter domain name:")
ip=socket.gethostbyname(domain)
print("ip address of",domain,"is",ip)
