from tkinter import *
import time
from PIL import Image, ImageTk

w=700
h=600
xVelo = 5       #directions
yVelo = 3


# ..........................................................
# Functions 
# ..........................................................

# convert func
def convertImg():
    pass

# bgRemove func
def bgRemove():
    pass

# func to flip image
def flipimg():
    pass


# ..........................................................
# window
# ..........................................................
root = Tk()
root.geometry(f"{w}x{h}")
root.minsize(w,h)
root.resizable(False,False)


root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)

# canvas for obj
canvas = Canvas(root,
                width=w,
                height=h)

canvas.grid(row=0, column=0, padx=0, pady=0, sticky="snew")

# photoimage for background
bgImg = Image.open("background.jpg")
bgResize = bgImg.resize((w,h))
bgphoto = ImageTk.PhotoImage(bgResize)
bgImg = canvas.create_image(0, 0, image=bgphoto, anchor=NW)

# getting image
image = Image.open("fish2.png")
# Resize the image using resize() method
resize_image = image.resize((100, 100))
# convert to photoimage
photo = ImageTk.PhotoImage(resize_image)
myImg = canvas.create_image(0, 0, image=photo, anchor=NW)



while True:
    # getting image coords
    coords = canvas.coords(myImg)
    print(coords)

# for width
    if(coords[0]>=w or coords[0]<0):
        # image = image.transpose(method=image.Flip_Left_Right)     #flip image
        xVelo = xVelo*-1

    
# for heigh
    if(coords[1]>=h or coords[1]<0):
        yVelo = yVelo*-1

# xVelo and yVelo in infinite direction
    canvas.move(myImg, xVelo, yVelo)

    root.update()
    time.sleep(0.08)


root.mainloop()