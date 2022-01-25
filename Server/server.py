
from tkinter import *
import tkinter
import socket
import threading
import time

host = '127.0.0.1'
port = 8882
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(0)
s.bind(('', port))
s.listen(1)


root = Tk()
root.geometry("300x500")
root.title(" Sever ")
  

  
Output = Text(root, height = 55, 
              width = 37, 
              bg = "white")
  

  

Output.pack()




T=True
try:
    root.update()
    while True:
        if T:
            try:
                c, addr = s.accept()
                
                T=False
            except:
                pass
        else:   
            try:
                t=c.recv(1024)
                c.settimeout(0)
                T=True
                root.update()
                Output.insert(END,"ProxyRequest File : " + t.decode('utf-8') + '\n')
                root.update()
                try:
                    f = open(t.decode('utf-8'))
                    c.send(f.read().encode())
                    root.update()
                    Output.insert(END,"File is found" + '\n')
                    root.update()
                except:
                    c.send("File is not found".encode())
                    root.update()
                    Output.insert(END,"File is  Not found" + '\n')
                    root.update()

                print(t.decode())
            # 
            except:
                i=0
        root.update()
except:
    pass


root.mainloop()



