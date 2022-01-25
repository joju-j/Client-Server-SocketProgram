import socket
from tkinter import *
import tkinter


host = 'local host'
port = 5000
  
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.connect(('127.0.0.1', port))


root = Tk()
root.geometry("400x300")
root.title(" Client ")

  
def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    s.send(INPUT.encode())
    t=s.recv(1024)
    inputtxt.delete("1.0","end")        
    Output.insert(END,INPUT+ '\n' + t.decode('utf-8') + '\n')
    

inputtxt = Text(root, height = 4,
                width = 35,
                bg = "light yellow")
  
Output = Text(root, height = 15, 
              width = 57, 
              bg = "#d6ff94")
  
Display = Button(root, height = 4,
                 width = 15 ,
                 text ="Request",
                 command = lambda:Take_input())
  

Output.pack()
inputtxt.pack(side=tkinter.LEFT)
Display.pack(side=tkinter.RIGHT)


root.mainloop()

