import socket 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 8000))
server_socket.listen(1)
print("Listening on port 8000")


while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode('utf-8')

    print(request)

    response = "HTTP/1.0 200OK\n\nHello World"
    client_connection.sendall(response.encode('utf-8'))
    client_connection.close()

