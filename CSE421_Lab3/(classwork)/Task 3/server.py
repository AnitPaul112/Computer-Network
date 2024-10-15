import socket
import threading

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

def handle_clients(conn,addr):
    
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
                vowels = "aeiouAEIOU"
                count = 0
                for i in msg:
                    if i in vowels:
                        count += 1
                if count == 0:
                    conn.send("Not enough vowels".encode(format)) 
                elif count <= 2:
                    conn.send("Enough vowels I guess".encode(format)) 
                else:
                    conn.send("Too many vowels".encode(format))             
                
    conn.close()            
while True:
    conn, addr = server.accept()
    thread = threading.Thread(target= handle_clients, args = (conn, addr))
    thread.start()



