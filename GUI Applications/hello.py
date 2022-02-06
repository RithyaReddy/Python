from tkinter import *
mw = Tk()

text = Label(mw, text="Enter your Name", font=("Arial",14))
text.pack()

user_input = Entry(mw, width=20, font=("Arial",20))
user_input.pack(padx=10,pady=10)

def say_hello():
    name = user_input.get()
    greeting = "Hello "+name+ "!"
    if name != "":
        text.config(text=greeting)
        user_input.delete(0, END)
    else:
        text.config(text="Enter your name")

btn = Button(mw, text="Click", font=("Arial",12),command=say_hello)
btn.pack(pady=20)

mw.mainloop()