import  socket 
import threading

nickname = input("enter your nickname: ")


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if(message == 'nick'):
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured !!!!!")
            client.close()
            break



def write():
    while True:
        message = (f"{nickname} : {input('')}")
        client.send(message.encode('ascii'))
    


receiveThread = threading.Thread(target=receive)
receiveThread.start()

writeThread = threading.Thread(target=write)
writeThread.start()

