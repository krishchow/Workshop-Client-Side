import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import os
from GUIClasses import JsonEditor,EntryWithPlaceholder
from tkinter.scrolledtext import ScrolledText
from APIHelper import *
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
        self.root.geometry('700x600')
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
        topFrame.pack(side='top',fill='x')

        bodyFrame = tk.Frame(root, background=self.bg)
        buttonFrame = tk.Frame(bodyFrame,background=self.bg)

        jsonFrame = tk.Frame(bodyFrame,background=self.bg)
        jsonText = JsonEditor(jsonFrame,bg='#ecf0f1')
        jsonText.init()
        tk.Button(buttonFrame,text="Validate Json",width=25,height=3,command=jsonText.validate_json).pack(side='top')
        tk.Button(buttonFrame,text="Indent Json",width=25,height=3,command=jsonText.indent_json).pack(side='top')
        

        res = ScrolledText(jsonFrame,height=10,bg='#ecf0f1')
        res.pack(side='bottom',fill='x',expand=True)
        jsonText.pack(fill='both',expand=True)
        jsonText.setError(res)

        buttonFrame.pack(side='left',padx=0, pady=0,fill='both',expand=True)
        jsonFrame.pack(side='right',padx=0, pady=0,fill='both',expand=True)
        
        bodyFrame.pack(side='top', fill='both',expand=True)
        root.pack(fill='both',expand=True)

if __name__ == '__main__':
    background = '#ffffff'
    foreground = '#ffffff'
    blueBackground = '#0968a3'
    a = Application()
