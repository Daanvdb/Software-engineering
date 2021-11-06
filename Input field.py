from tkinter import *
from tkinter import messagebox
#make some kind of whatsapp --> one box for input and one for output
root = Tk()

e = Entry(root, cursor= 'dot',selectbackground='blue', selectforeground='white',  width=100, borderwidth = 5)
e.pack()
e.insert(0, 'Enter what you want us to search for and press the button')

def myClick():
    search = "Search " + e.get()
    myLabel = Label(root, text = search)
    myLabel.pack()
    
def popup():
    messagebox.showinfo("Help", "Here you should be able to search for help")

myButton = Button(root, text = "Search ", command=myClick).pack()
#button_quit = Button(root, text= "Exit program", command=root.quit).pack()
Button(root, text= "Help", command=popup).pack()



root.mainloop()