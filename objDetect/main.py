from tkinter import *
import time
from PIL import Image, ImageTk
from rembg import remove
import cv2
from fish import *


# get resize image func
def getImg(img):
    # getting image
    image = Image.open(img)
    # Resize the image using resize() method
    resize_image = image.resize((100, 100))

    # Save the resized image to a file
    resize_image.save(img)

    # return img name after saving img
    return img

# ..........................................................
# window
# ..........................................................
root = Tk()

w=700
h=600

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


# getting img open
# img = "fish2.png"
# myImg_name = getImg(img)

# resized_image = Image.open(myImg_name)

# converting to photo
# photo = ImageTk.PhotoImage(resized_image)


fish1 = Fish(canvas,0,0,5,3,"paperfish.webp")

# convert
# get img
# bg remove
# photo convert
# move


fish1.convertImg()
fish1.getImg()
fish1.bgRemove()
fish1.photoImg()



while True:
    fish1.move()
    # updating window
    root.update()
    time.sleep(0.03)

root.mainloop()