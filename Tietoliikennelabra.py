import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("172.20.241.9", 20000))
    s.sendall(b"56\n")
    data = s.recv(1024)

list = []
list.append(data.decode("utf-8"))

for i in list:
    print(i, end = "")

s.close

#toimi myös teemun esimerkillä. sillä kyllä sai enemmän dataa ulos kuin tuon 1 rivin

        
