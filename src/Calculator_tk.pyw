#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox,ttk

import parse
import re
import sys

help_string="""
Application Calculator
Version 1.0

Enter mathematical expression and press enter
or button '=' to evaluate it.

Clear expression by pressing 'C'

functions:
    sqrt(x) - square root of 'x'
    log(x) - decimal logarithm of 'x' 
    ln(x) - natural logarithm of 'x'
    power(x,exp) - 'x' to the power of 'exp'
    nroot(base,x) - 'base'-th root of 'x'
    fact(x) - factorial of 'x'

operators:
    +,-,*,/,^

other tokens:
    , - separate function parameters
    ( - left bracket or function call
    ) - right bracket
"""

top = Tk()
top.title("Calculator")
top.iconbitmap('icon.ico')

m=0
show_err=False

err_size=22
def_size=22

expr=Entry(top,justify=RIGHT,font=("Courier",def_size))
expr.grid(row=1,column=0,columnspan=4,sticky="nesw",padx=5,pady=5)
expr.focus()

def eval():
    global expr    
    global show_err    
    val=expr.get()
    expr.delete(0,END)
    try:
        res=parse.Parser().parse(val)
        expr.insert(0,re.sub(r"\.0*$","",str(res)))
    except SyntaxError as err:
        show_err=True
        expr.configure(font=("Courier",err_size))
        expr.insert(0,str(err))
    except ZeroDivisionError as err:
        show_err=True
        expr.configure(font=("Courier",err_size))
        expr.insert(0,str(err))
    except ValueError as err:
        show_err=True
        expr.configure(font=("Courier",err_size))
        expr.insert(0,str(err))

def down(e):
    global expr
    global show_err
    
    if isinstance(e.char,str) and e.char:
        if show_err:
            expr.delete(0,END)
            expr.configure(font=("Courier",def_size))
            show_err=False
            return
        if ord(e.char)==13:
            eval()
        elif ord(e.char)==27:
            sys.exit(0)


top.bind('<KeyPress>', down)




def button_pressed(name):
    if not name:
        return
    if name=="help":
        
        messagebox.showinfo("Help",help_string)
        return
    global expr
    global show_err
    if show_err:
        expr.delete(0,END)
        expr.configure(font=("Courier",def_size))
        show_err=False
    if name=="=":
        eval()
        return
    if name=="C":
        expr.delete(0,END)
        return
    
    expr.insert(INSERT,name+("(" if len(name)>1 else ""))

def create_button(name,row,col,pad=2,font=("Courier",20)):
    button=Button(top,text=name,command=lambda x=name:button_pressed(x),font=font)
    button.grid(row=row,column=col,sticky="nesw",pady=pad,padx=pad)
    

create_button("help",0,0,0,("Courier",10))
buttons=[
    ["sqrt","log","ln","C"],
    ["fact","nroot","power","^"],
    ["(",",",")","*"],
    ["7","8","9","/"],
    ["4","5","6","+"],
    ["1","2","3","-"],
    ["","0",".","="],
]

top.rowconfigure(1, weight=1)
for i,r in enumerate(buttons):
    top.rowconfigure(i+2, weight=1)
    for j,c in enumerate(r):
        top.columnconfigure(j, weight=1)
        create_button(c,i+2,j)


top.geometry("400x600")
top.mainloop()
