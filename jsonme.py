'''
Source: https://gist.github.com/jul/e9132abe8b5aeea573917191591fb90b
Credits: https://gist.github.com/jul

I migrated the code to python 3.6 and created a class!
'''
import os
import re
from json import dumps, loads
import sys

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import messagebox

# create a menu & define functions for each menu item

def indent_json():
    if validate_json():
        str_json = text.get("1.0",tk.END)
        clear(text)
        clear(res)
        text.insert('1.0', dumps(loads(str_json), indent=4))
        log("Indentation done")
    else: 
        log("please correct errors first")
    
def clear(text_stuff):
    text_stuff.delete("1.0", tk.END)
    
def log(msg):
    res.insert("1.0", (type(msg) is str and msg or repr(msg))+ "\n")

def tab(arg):
    text.insert(tk.INSERT, " " * 4)
    return 'break'

delim_re = re.compile(
'''
line\s(?P<line>\d+)\s
column\s(?P<col>\d+)\s
\(
    char\s(?P<before>\d+)
        (\s\-\s(?P<after>\d+))? # optionally followed by a range
\)''', re.VERBOSE) 

def validate_json():
    clear(res)
    str_json = text.get("1.0",tk.END)
    text.tag_delete("error")

    try:
        loads(str_json)
    except ValueError as e:
        clear(res)
        log(e.args)
        mark = delim_re.search(e.args)
        if not mark:
            mark = dict(before = "0", after = "end", line = "0", col = "0")
        else:
            mark = mark.groupdict()
            mark["after"] =  "1.0 +%sc" % (mark["after"] or (int(mark["before"]) +1))
        
        before = "1.0 +%(before)sc" % mark
        has_delim = re.search("Expecting '(?P<delim>.)'", e.args)
        if has_delim:
            after = mark["after"] = "1.0 +%dc" % (int(mark["before"]) +1)
        
            text.insert(before,has_delim.groupdict()["delim"])
            #text.delete(after)
        after = "%s" % mark["after"]
        text.tag_add("error", before, after)
        text.tag_config("error", background="yellow", foreground="red")
        return False
    except Exception as e:
        log(e)
        return False
    log("JSON is valid")
    return True

class JsonEditor(ScrolledText):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<FocusOut>", self.indent_json)
        self.bind("<Tab>", self.tab)
        #self.bind("<Key>",self.validate_json)
        self.delim_re = re.compile(
        '''
        line\s(?P<line>\d+)\s
        column\s(?P<col>\d+)\s
        \(
            char\s(?P<before>\d+)
                (\s\-\s(?P<after>\d+))? # optionally followed by a range
        \)''', re.VERBOSE)

    def indent_json(self,*args):
        if self.validate_json():
            str_json = self.get("1.0",tk.END)
            clear(self)
            clear(res)
            self.insert('1.0', dumps(loads(str_json), indent=4))
            log("Indentation done")
        else: 
            log("please correct errors first")

    def validate_json(self,*args):
        clear(res)
        str_json = self.get("1.0",tk.END)
        self.tag_delete("error")
        try:
            loads(str_json)
        except ValueError as e:
            clear(res)
            msg = str(e.args)
            log(msg)
            mark = self.delim_re.search(msg)
            if not mark:
                mark = dict(before = "0", after = "end", line = "0", col = "0")
            else:
                mark = mark.groupdict()
                mark["after"] =  "1.0 +%sc" % (mark["after"] or (int(mark["before"]) +1))
            
            before = "1.0 +%(before)sc" % mark
            has_delim = re.search("Expecting '(?P<delim>.)'", msg)
            if has_delim:
                after = mark["after"] = "1.0 +%dc" % (int(mark["before"]) +1)
            
                self.insert(before,has_delim.groupdict()["delim"])
                #text.delete(after)
            after = "%s" % mark["after"]
            self.tag_add("error", before, after)
            self.tag_config("error", background="yellow", foreground="red")
            return False
        except Exception as e:
            log(e)
            return False
        log("JSON is valid")
        return True
        
    def tab(self,arg):
        self.insert(tk.INSERT, " " * 4)
        return 'break'

pref = dict(padx=5, pady=5)
root = tk.Tk(className=u"Minimal customized JSON editor")
upper = tk.Frame(root, relief=tk.GROOVE)
bottom = tk.Frame(root, relief=tk.GROOVE)

text= JsonEditor(upper, width=100, height=40)
#text= ScrolledText(upper, width=100, height=40)
#text.bind("<Tab>", tab)
res= ScrolledText(bottom, width=100,height=10)

validate = tk.Button(upper, text = "Validate", command=text.validate_json)
indent = tk.Button(upper, text = "Indent", command=text.indent_json)


res.pack(side=tk.LEFT,**pref)
upper.pack(side=tk.TOP,**pref)
bottom.pack(side=tk.BOTTOM, **pref)
text.pack(side=tk.TOP,fill="y",**pref)
validate.pack(side=tk.LEFT)
indent.pack(side=tk.LEFT)
text.insert("1.0", """{ 
"a" : 1
    "b" ; 2
}""")
root.mainloop()

