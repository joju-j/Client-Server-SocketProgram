
from tkinter import *
import tkinter
import socket
import threading
import time

host = '127.0.0.1'
port = 5000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(0)
s.bind(('', port))
s.listen(1)


root = Tk()
root.geometry("300x500")
root.title(" Proxy ")
  

  
Output = Text(root, height = 55, 
              width = 37, 
              bg = "#e8e8e8")
  


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
                if not t.decode():
                    T=True
                    continue
                t=t.decode('utf-8')
                
                root.update()
                Output.insert(END,"Client Request File : " + t + '\n')
                root.update()
                try:
                    f = open(t)
                    c.send(f.read().encode())
                    root.update()
                    Output.insert(END,"File is found" + '\n')
                    root.update()
                except:
                    try:
                        time.sleep(1)
                        root.update()
                        Output.insert(END,"File not found in proxy" + '\n')
                        root.update()
                        time.sleep(1)
                        root.update()
                        Output.insert(END,"Connecting to Server.." + '\n')
                        root.update()
                    
                        k = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                        k.connect(('127.0.0.1', 8882))
                       
                        k.send(t.encode())
                        g=k.recv(1024)
                        if g.decode()!="File is not found":
                            f = open(t, "a")
                            f.write(g.decode())
                            f.close()
                            root.update()
                            Output.insert(END,"File is created" + '\n')
                            root.update()
                            c.send(g)
                        else:
                            root.update()
                            Output.insert(END,"File Not in Server "+ '\n')
                            root.update()
                            c.send(g) 
                        
                    except:
                        root.update()
                        Output.insert(END,"Connection Error to Server" + '\n')
                        root.update()
                        c.send("File not Found".encode())
                print(t.decode())
            # 
            except:
                i=0
    root.update()
except:
    pass


root.mainloop()



