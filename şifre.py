from tkinter import *
import random
import string

root = Tk()
root.geometry("400x280")
root.title("Password Generator")

title = StringVar()
choice = IntVar()
lengthlabel = StringVar()
passlength = IntVar()
symbols = "!§$%&/()=?{[]}*+'#~,;.:-_'<>"
poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
advanced = poor + average + symbols

def selection():
    choice.get()


def callback():
    Isum.config(text=passgen())


Isum = Label(root, text="")
Isum.pack(side=BOTTOM)

password = str(callback)

def passgen():
    global password
    password = ""
    if choice.get() == 3:
        return password.join(random.sample(advanced, passlength.get()))


def copytoclipboard():
    global password
    print(password)
    Isum.clipboard_clear()
    Isum.clipboard_append(password)
    Isum.update()


label = Label(root, textvariable=title).pack()
title.set("The strength of the password:")


R3 = Radiobutton(root, text="Uppercase, Lowercase, Digits, Symbols", variable=choice, value=3, command=selection).pack(
    anchor=CENTER)

lengthlabel.set("Password length: (8 to 24)")
lengthtitle = Label(root, textvariable=lengthlabel).pack()

spinboxlength = Spinbox(root, from_=8, to_=24, textvariable=passlength, width=13).pack()

passgenButton = Button(root, text="Generate Password", command=callback)
passgenButton.pack()

copyButton = Button(root, text="Copy Password to Clipboard", command=copytoclipboard)
copyButton.pack(side=BOTTOM)

 
root.mainloop()
"""random.choices(R3, weights = [2, 2, 2, 4], k = 10))"""


