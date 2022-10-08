import datetime
import time
import tkinter
import threading

app = tkinter.Tk()
app. overrideredirect (True)
app. attributes('-alpha', 0.7)
app. attributes('-topmost', 1)
app. geometry('200x100+100+100')
app.config(background = "pink")


labelDateTime = tkinter. Label( app, width=130)
labelDateTime. pack(fill=tkinter . BOTH, expand=tkinter. YES)
labelDateTime. configure(bg = 'gray')
X = tkinter . IntVar(value=0)
Y = tkinter. IntVar(value=0)

canMove = tkinter . IntVar(value=0)

still = tkinter . IntVar(value=1)

def onLeftButtonDown(event):
    app. attributes('-alpha', 0.4)
    X. set(event.x)
    Y. set(event.y)
    canMove . set(1)

labelDateTime . bind(' <Button-1>', onLeftButtonDown)

def onLeftButtonUp( event):
    app. attributes('-alpha', 0.9)
    canMove. set(0)

labelDateTime. bind( '<ButtonRelease-1>', onLeftButtonUp)

def onLeftButtonMove(event):
    if canMove.get()==0:
        return
    newX = app.winfo_x()+(event.x-X.get())
    newY = app . winfo_y( )+(event.y-Y. get())
    g ='130x25+'+str(newX)+'+'+str(newY)
    app . geometry(g)

labelDateTime . bind(' <B1 -Motion>', onLeftButtonMove)

def onRightButtonDown( event):
    still.set(0)
    t.join(0.2)
    app.destroy()

labelDateTime . bind('<Button-3>',onRightButtonDown)

def nowDateTime():
    while still.get()==1:
        s = str(datetime.datetime.now())[:19]
        labelDateTime[ 'text'] = s
        time . sleep(0.2)

t = threading.Thread(target=nowDateTime)
t. daemon = True
t.start()
app.mainloop()