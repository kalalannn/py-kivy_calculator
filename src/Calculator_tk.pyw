"""
    Projekt IVS 2019

    Tým: /(o_o)/

    Autoři:
        - Martin Krbila
	- Jirka Hába
	- Artsiom Luhin
	- Nikolaj Vorobiev
"""

##
#   @file Calculator_tk.pyw
#   @author Martin Krbila
#   @date 22.4.2019
#
#   @brief Calculator GUI
#
#   Contains GUI for simple calculator

#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox,ttk

import parse
import re
import sys

## Help displayed to user
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

## Root window
top = Tk()
top.title("Calculator")
top.iconbitmap('icon.ico')

show_err=False

err_size=22
def_size=22

## Entry box for user
expr=Entry(top,justify=RIGHT,font=("Courier",def_size))
expr.grid(row=1,column=0,columnspan=4,sticky="nesw",padx=5,pady=5)
expr.focus()

##
#   @brief Evaluate expression
#
#   Evaluate currently displayed expression
#   @post Numerical value of expression in expr is displayed in expr
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

##
#   @brief Key press event
#
#   Key press event
def down(e):
    global expr
    global show_err
    
    if isinstance(e.char,str) and e.char:
        # is error displayed
        if show_err:
            expr.delete(0,END)
            expr.configure(font=("Courier",def_size))
            show_err=False
            return

        # was enter pressed
        if ord(e.char)==13:
            eval()

        # was escape pressed
        elif ord(e.char)==27:
            sys.exit(0)

# bind key event
top.bind('<KeyPress>', down)



##
#   @brief Button pressed event
#
#   Reacts to GUI button press
#   @param name Name of the button pressed
def button_pressed(name):
    if not name:
        return

    # show help
    if name=="help":
        
        messagebox.showinfo("Help",help_string)
        return
    global expr
    global show_err

    # remove previous error message if any
    if show_err:
        expr.delete(0,END)
        expr.configure(font=("Courier",def_size))
        show_err=False

    # evaluate if "=" was pressed
    if name=="=":
        eval()
        return

    # Clear expression if "C" was pressed
    if name=="C":
        expr.delete(0,END)
        return

    # Insert new character
    expr.insert(INSERT,name+("(" if len(name)>1 else ""))

##
#   @brief Create new button
#
#   Create new button in specified grid position
#   @param name Name of the button and text content
#   @param row Row in the window grid
#   @param col Column in the window grid
#   @param pad pixels to pad around button
#   @param font Font to use in the button
def create_button(name,row,col,pad=2,font=("Courier",20)):
    button=Button(top,text=name,command=lambda x=name:button_pressed(x),font=font)
    button.grid(row=row,column=col,sticky="nesw",pady=pad,padx=pad)
    
# Create help button
create_button("help",0,0,0,("Courier",10))

## Calculator button matrix
buttons=[
    ["sqrt","log","ln","C"],
    ["fact","nroot","power","^"],
    ["(",",",")","*"],
    ["7","8","9","/"],
    ["4","5","6","+"],
    ["1","2","3","-"],
    ["","0",".","="],
]

# Setup button matrix
top.rowconfigure(1, weight=1)
for i,r in enumerate(buttons):
    top.rowconfigure(i+2, weight=1)
    for j,c in enumerate(r):
        top.columnconfigure(j, weight=1)
        create_button(c,i+2,j)


# Draw window
top.geometry("400x600")
top.mainloop()
