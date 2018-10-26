
import socket 

def sock_init(IP)
    t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (IP,Port)

    InputBuffer= 2018880

    t.b6ind(address) 
    t.listen(1)

client, addr = t.accept()
print ("bollocks")
while True:
    data = client.recv(512)
    print (data) 
    print ("starting to process data")
    if( data=="Hello server"):
        client.send("Hello Bitch")
        
    elif(data=="discoennected"):
        client.send("good bye")
    else:
        client.send("Invalid data")
        

        