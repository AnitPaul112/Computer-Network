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
                
                hours_worked = int(msg)  
                if hours_worked <= 40:
                    salary = hours_worked * 200
                else:
                    salary = 8000 + (hours_worked - 40) * 300

                    
                conn.send(f"Salary for {hours_worked} hours worked is: Tk {salary}".encode(format))
                
    conn.close()

                    


                   
                

            



