from tkinter import *
import time
from fish import *
from PIL import Image, ImageTk
import cv2

# func to get img
def getimg(img):
    # getting image
    image = Image.open(img)
    # Resize the image using resize() method
    resize_image = image.resize((80, 80))
    # convert to photoimage
    photo = ImageTk.PhotoImage(resize_image)

    return photo


root = Tk()

w=500
h=500

root.title("imgVisualization")
root.geometry(f"{w}x{h}")
root.minsize(w,h)
root.resizable(False,False)


# canvas for obj
canvas = Canvas(root,
                width=w,
                height=h)
canvas.pack()

# photoimage for background
bgImg = Image.open("background.jpg")
bgResize = bgImg.resize((w,h))
bgphoto = ImageTk.PhotoImage(bgResize)
bgImg = canvas.create_image(0, 0, image=bgphoto, anchor=NW)
# volley = ball(canvas,0,0,100,5,2,"light blue")
# basket = ball(canvas,0,0,50,4,2,"orange")
# cricket = ball(canvas,0,0,80,1,2,"grey")

# img to pass in getimg()
# img1 = "fish2.png"



# get img as photo
photo1 = getimg("fish1.png")
photo2 = getimg("fish2.png")
photo3 = getimg("fish3.png")

# using class fish and passing values to init
fish1 = Fish(canvas,0,0,8,3,photo1)
fish2 = Fish(canvas,0,0,3,3,photo2)
fish3 = Fish(canvas,w,0,3,7,photo3)

while True:
    # volley.move()
    # basket.move()
    # cricket.move()
    fish1.move()
    fish2.move()
    fish3.move()

    # contineously updating window
    root.update()
    time.sleep(0.05)

root.mainloop()