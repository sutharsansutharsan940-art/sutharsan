import os
host=input("enter host to ping:")
responce=os.system(f"ping-c 2{host}")
if responce==0:
    print("host is reacheble")

else:
    print("host is not rechable")
    
