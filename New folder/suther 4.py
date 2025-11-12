import socket
target=input("enter ip address:")
port=int(input("enter port number:"))
sock=socket.socket(socket.AF_INET,socket.sock_stream)
result=sock.connect_ex((target,port))
if result==0:
  print(f" port{port} is open on{target}")

else:
    print(f"port{port} is open on{target}")
    sock.close()
