import socket
import threading

localHost = '127.0.0.1'
port = 55555

server  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((localHost,port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)



def accept(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat.'.encode('ascii'))
            print (f'{nickname} disconnected .')
            nicknames.remove(nickname)
            break



def receive():
    while True:
        client , address = server.accept()
        print(f'{str(address)} connected to server')

        client.send("nick".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat.".encode('ascii'))
        client.send("Welcome to the server !".encode('ascii'))

        thread = threading.Thread(target=accept , args=(client,))
        thread.start()


print("server is listening......")
receive()







