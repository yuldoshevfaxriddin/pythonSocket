import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1",12345))

server.listen()

while True:
    user, address = server.accept()
    print("connect",user,address)
    user.send(input("server>> ").encode("utf-8"))
    data = user.recv(1024)
    print('user: ',data.decode("utf-8"))
