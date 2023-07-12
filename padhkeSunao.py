# Read what you write
# installed pipenv to install pywin for win32com
from pickle import TRUE                     
from win32com.client import Dispatch        #to get type of voice to speak
import time     #for time
import tkinter as tk
import customtkinter as ctk     #for window


speak = Dispatch("Sapi.SpVoice")    #arg is voice type


# ........................
#main root window
root = ctk.CTk()
root.title("cmd")
root.geometry("450x300")
root.resizable(False,False)
# root.rowconfigure((0,1,2,3), weight=1)
root.columnconfigure((0,1,2,3), weight=1)


# label for operatng system
label = ctk.CTkLabel(root,
                    text="Padhke Sunao:",
                    font=("Roboto",17,"bold"))
label.grid(row=0,column=0, columnspan=2,padx=10, pady=30)


# entry feild
entry = ctk.CTkEntry(root,
                     height=80,
                    placeholder_text="enter text to read")
entry.grid(row=1,column=0,columnspan=4,padx=40, pady=(20),sticky="ew")


# read("Welcome...Enter the text to read!")

# read function
def read():
    str = entry.get()
    speak.Speak(str)


# submit btn
submitBtn = ctk.CTkButton(root,
                          text="submit",
                          command=read)
submitBtn.grid(row=2,column=0,columnspan=2,padx=15, pady=(10))



# clear func
def clear():
    # clears entry
    entry.delete(0,"end")


# clear btn
clearBtn = ctk.CTkButton(root,
                          text="Clear",
                          command=clear)
clearBtn.grid(row=2,column=2,columnspan=2,padx=20, pady=(10))


root.mainloop()





