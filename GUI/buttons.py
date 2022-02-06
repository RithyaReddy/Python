from tkinter import *
#creating main window
mw = Tk()

def click():
    mylabel = Label(mw, text="Virtual Reality", font=("Arial",12))
    mylabel.pack(pady=10)

#creating input
user_input = Entry(mw, width=15, font=("Arial",18))
user_input.pack(pady=10)

#creating buttons
my_button = Button(mw, text="Click me !", padx=15,pady=10,font=("Arial",12), command=click) #creating space inside button
my_button.pack(padx=30, pady=30)

mw.mainloop()