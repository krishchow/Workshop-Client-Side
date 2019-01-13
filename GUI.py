import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import os
from GUIHelper import *
changedfont = 'ms sans serif'

class Application():
    def __init__(self):
        self.root = tk.Tk()
        self.keyVar = tk.StringVar()
        self.key = ""
        self.serverVar = tk.StringVar()
        self.serverIp = ""
        def callbackKey(*args):
            key=self.keyVar.get()
            return True
        self.keyVar.trace_add("write", callbackKey)
        def callbackServer(*args):
            serverIp=self.serverVar.get()
            return True
        self.keyVar.trace_add("write", callbackServer)
        self.root.title("PokeSearch")
        self.root.style = ttk.Style()
        self.root.style.theme_use('clam')
        self.root.geometry('500x500')
        self.bg = background
        self.loadMain()
        tk.mainloop()
    
    def loadMain(self):
        root = tk.Frame(self.root, background=self.bg)
        mainFrame = tk.Frame(root, background=self.bg)
        header = ttk.Label(mainFrame, text="Welcome the PokeSearch Application",background=self.bg, font=(changedfont, 24, "bold"))
        header.pack()
        mainFrame.pack(side='top')
        topFrame = tk.Frame(root, background=self.bg)
        keyEnt = EntryWithPlaceholder(topFrame, background=self.bg, font=(changedfont, 18, "bold"), textvariable=self.keyVar)
        keyEnt.setPlaceholder("User Key")
        keyEnt.pack(side='left',fill='x',expand=True)
        serverEnt = EntryWithPlaceholder(topFrame, background=self.bg, font=(changedfont, 18, "bold"), textvariable=self.serverVar)
        serverEnt.setPlaceholder("Server IP")
        serverEnt.pack(side='left',fill='x',expand=True)
        topFrame.pack(side='top',fill='both')
        bottomFrame = tk.Frame(root, background=self.bg)
        #ttk.Button(bottomFrame, text="Log Out", command=t,style='Main.TButton').pack(side='right')
        #ttk.Button(bottomFrame, text="Add A New Account", command=lambda id=ID: addAccount(id,self.db),style='Main.TButton').pack(side='left')
        bottomFrame.pack(side='bottom',fill='x')
        bodyFrame = tk.Frame(root, background=self.bg)
        bodyFrame.pack(fill='both')
        root.pack(fill='both',expand=True)

if __name__ == '__main__':
    background = '#ffffff'
    foreground = '#ffffff'
    blueBackground = '#0968a3'
    a = Application()
