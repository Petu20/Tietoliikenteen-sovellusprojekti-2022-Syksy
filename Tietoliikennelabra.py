import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.20.241.9", 20000))
s.sendall(b"toimiiko")

data = s.recv(1024)
print("Received {data!r}") [699:] #palauttaa viimeiset 300 riviä

s.close

    
  

        