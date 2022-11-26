# digital clock

# time for system date and time
from time import strftime

# for GUI
from tkinter import *


# craeting a window
root = Tk()
root.title("Time dekho zara")
root.geometry("400x250")
root.configure(bg="black")
# root.resizable(False,False)




# creating a label
clock = Label(root, bg="black", fg="white", font=("Times New Roman", 40,"bold"), relief="flat")
clock.place(x=90,y=110)

# function to update 24 hour time (kind of recurrsion)
def update():
    # time format
    now = strftime("%H:%M:%S")

    # to display text on screen
    clock.configure(text = now)

    # update function after every 80 miliseconds
    clock.after(80, update)


# function to update 12 hour time (kind of recurrsion)
def update_12():
    # time format
    now = strftime("%I:%M:%S")

    # to display text on screen
    clock.configure(text = now)

    # update function after every 80 miliseconds
    clock.after(80, update_12)

# buttons for format
b1 = Button(root, text="24 hour",fg="black", padx=12, borderwidth=3, command=update)
b1.pack(side=TOP, padx=20, pady=20)

b2 = Button(root, text="12 hour",fg="black", padx=12, borderwidth=3, command=update_12)
b2.pack(side=TOP ,padx=20, pady=0)


root.mainloop()
