import socket

port = 5555
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
buffer = 16
format = "utf-8"
disconnected = "End"

server_socket_address = (host_ip, port)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(server_socket_address)

server.listen()
print("server is active now")

while True:
    conn, addr = server.accept()
    print("Connected to", addr)
    connected = True
    while connected:
        message_lenght = conn.recv(buffer).decode(format)
        print("lenght of the message", message_lenght)

        if message_lenght:
            message_lenght = int(message_lenght)
            msg = conn.recv(message_lenght).decode(format)
            if msg == disconnected:
                conn.send("Goodbye.".encode(format))
                print("terminating connection with", addr)
                connected = False
            else:
                print(msg)
                conn.send("Recieved the message".encode(format))
    conn.close()            



