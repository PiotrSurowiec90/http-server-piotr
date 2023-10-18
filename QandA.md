
What does AF_INET and SOCK STREAM constants in socket socket_function stands for?
```
AF_INET IP address family - (IPv4)

SOCK_STREAM - Indicates TCP socket.
```


What is socket.SOL_SOCKET, SO_REUSEADDR, 1 inside socket options?
```
SOL_SOCKET - constant representinf 'socket-level' option

SO_REUSEADDR - allows You to resuse address if the socket is closed and the server has not released the port yet.
```


Whay we have 1 as and argument in liten socket method?
```
It specifies number of connections server accepts at a time - 1 connectiona at a time.
```


Wat does the 'recv' method on client socket does?
```
We use it to recive data from the clinet, it takes number of bytes we accpet as an argument.
```