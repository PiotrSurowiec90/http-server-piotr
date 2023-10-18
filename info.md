## Sockets 
> A socket is an abstraction provided by your operating system that allows you to send and receive bytes through a network.

> A Socket is identified by IP address and Port Number.

> Server waits for incoming client requests by listening to a specified port. Once request is recived
>, the server accpets a connection from client socket to complete the connection.

> Python **socket** library helps us to work with sockets.


## Steps 
### Set up server socket
1. **CREATE SERVER SOCKET** - Create socket object, Specify it's address family to IPv4 and its type to TCP socket.
2. Set socket options to prevent '*Adress already in use error*'.
3. Bind socket to specific IP address and port alloowing the server to listen for incoming connections on that address and port.
4. Make the server socket start listening.
5. Log the message that server is listening on specified port.
<hr>

### ENTER an infinite loop to continiously  accept connections from client.
1. Accept incoming connections.
2. Recieve clinet request (For the sake of the exercise lets assume its simple one-liner request up to 1024 bytes)
3. Log request to the console.
4. Send basic HTTP respose with the status - 200 and Hello World! as a content.
5. Close the client connection.

