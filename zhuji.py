#在主机上操作
from socket import *
from tkinter import *
import tkinter
def server():
    IP = ''
    PORT = 50000
    BUFLEN = 512
    listenSocket = socket(AF_INET,SOCK_STREAM)
    listenSocket.bind((IP,PORT))
    listenSocket.listen(8)
    print(f'           ɹ     {PORT} ˿ڵȴ  ͻ       ...')
    dataSocket,addr =listenSocket.accept()
    print('    һ   ͻ       :',addr)
    while True:
        receved = dataSocket.recv(BUFLEN)

        if not receved:
            break

        info = receved.decode()
        print(f' յ  Է     Ϣ  {info}')

        dataSocket.send(f'    ˽  յ     Ϣ:{info}'.encode())

    dataSocket.close()
    listenSocket.close()
window =tkinter.Tk()
window.title('serverOperation')
window.geometry('1000x200')

button=tkinter.Button(window,text='主机上操作',bg='#CC33CC', command=lambda : server())
button.pack()

top=mainloop()
