from tkinter import *
from maintool_variables import * # Width and Height

root = Tk()
root.title('Calculator')
root.geometry('{}x{}'.format(ROOT_WIDTH, ROOT_HEIGHT))

# create all of the main containers
top_frame = Frame(
        root,
        bg='cyan',
        width=TOP_WIDTH,
        height=TOP_HEIGHT,
        pady=3
        )
button_frame = Frame(
        root,
        bg='blue',
        width=BUTTON_FRAME_WIDTH,
        height=BUTTON_FRAME_HEIGHT
        )
history_frame = Frame(
        root,
        bg='red',
        width=HISTORY_FRAME_WIDTH,
        height=HISTORY_FRAME_HEIGHT
        )

# grid
top_frame.grid(row=0, column=0, columnspan=2)
button_frame.grid(row=1, column=0, sticky=W)
history_frame.grid(row=1, column=1, sticky=E)

# buttons
buttons = []
for x in SIMPLE_BUTTONS:
    buttons.append(Button(
        button_frame,
        text=x,
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT
        ))

# buttons grid
r=0
c=0
for x in buttons:
    x.grid(row=r, column=c)
    c += 1
    if c == 4:
        c = 0
        r += 1

root.mainloop()
