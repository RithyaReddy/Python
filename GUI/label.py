from tkinter import *

#creating window
main_window = Tk()
mylabel = Label(main_window, text="First Python GUI", font=("Arial",20), padx=30, pady=50)
mylabel.pack(side=BOTTOM)

main_window.mainloop()      #helps to display the window