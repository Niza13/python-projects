# main filr for image editor tool

import customtkinter as ctk
import cv2      #form image editing
import numpy as np      # for arrays
import funcs as func


# main window
root = ctk.CTk()
root.geometry("650x600")
root.title("PyImage Editor")

ctk.set_appearance_mode("dark")

# label
label = ctk.CTkLabel(root,
                     text="PyImage Editor",
                     font=ctk.CTkFont("Roboto",22,"bold")).grid(row=0, column=0, padx=(20,20), pady=(30,10), sticky="snew")

# entry
entry = ctk.CTkEntry(root,
                    placeholder_text="Enter a image location: ",
                    text_color="grey80",
                    width=400)
entry.grid(row=1, column=0, padx=(30,20), pady=(20,20), sticky="enw")

# function to select image
def select():
    img = entry.get()
    print(img)  


# select image btn
selectBtn = ctk.CTkButton(root,
                            text="Select Image",
                            fg_color="orchid3",
                            hover_color="orchid4",
                            command=select)
selectBtn.grid(row=1, column=1, padx=(10,0), pady=(20,20), sticky="nw") 


 


root.mainloop()