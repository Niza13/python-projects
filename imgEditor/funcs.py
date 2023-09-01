# image editor tool with GUI using customtkinter and opencv, numpy and other libraries

import cv2      #form image editing
import numpy as np      # for arrays

imgName = 'img3.jpg'

# to get img
img = cv2.imread(imgName)

# it gives pixels array in BGR
print(img)
print(img.size)     #gives total size of image
print(img.shape)     #gives shape of image (row,column,channel)

# function to open and display image
def show(img):
    cv2.imshow("img", img)     #shows image as a window
    cv2.waitKey()               #so window will not be destroyed
    cv2.destroyAllWindows()     #to destroy window

    # btn func
    # show(img)

# function to convert image in other formats
def convert(img, imgName):

    imgName = imgName.split('.')[0]
    # print(imgName)

    # converting img
    cv2.imwrite(f'{imgName}.png',img)

    # btn func
    # convert(img,ImgName)


# function to resize image
def resize(img,x,y):

    resized = cv2.resize(img, (x,y))
    show(resized)

    # btn func
    # resize(img,400,300)


# image converting to black and white
def bAndW(img):
    
    grey =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    show(grey)

    # btn func
    # bAndW(img)


# function to get negative image
def negative(img):

    negativeImg = 1-img     #all coordinates to negative
    show(negativeImg) 

    # btn func
    # show(img)


# function to creae empty images
def emptyImg(x,y,channels,b,g,r):

    # creating a empty zero of x rows y columns and channels
    emptyImg = np.zeros((x,y,channels), dtype=np.uint8)
    # to fill image with color
    emptyImg[:] = [b,g,r]

    show(emptyImg)

    # btn func
    # emptyImg(300,300,3,168,88,62)


# function to add text on img
def txt(img, text, x,y, size, b,g,r):
    
    # img = emptyImg(300,300,3,255,255,255)
    # text to place on img
    text = cv2.putText(img,text, (x,y), cv2.FONT_HERSHEY_COMPLEX, size, (b,g,r))
    show(img)
    

    # btn func
    # txt(img, "hello", 100,100,2,53,64,23)


# function to horizontal concatenate img
def channel(img1,img2):

    resized1=resize(img1,300,300)
    resized2=resize(img2,300,300)

    # contat horizontally
    horizontal = cv2.hconcat([resized1,resized2])
    # contat vertically
    vertical = cv2.vconcat([resized1,resized2])

    show(horizontal)
    show(vertical)


    # channel(img,img)



# function to crop img
def crop(img):

    # gives numbers of selected area
    ratio = cv2.selectROI(img,False)
    print(ratio)
    # cropping image
    croppedImg = img[ratio[1]:ratio[1]+ratio[3], ratio[0]:ratio[0]+ratio[2]]

    show(croppedImg)


    # crop(img)


# function to rotate image
def rotate(img):

    left = cv2.ROTATE_90_CLOCKWISE              #rotate left
    right = cv2.ROTATE_90_COUNTERCLOCKWISE      #rotate right
    rotatedLeft = cv2.rotate(img ,left )
    rotatedRight = cv2.rotate(img ,right )
    show(rotatedLeft)
    show(rotatedRight)

    # rotate(img)


# function to flip image
def flip(img):

    verticalFlip = cv2.flip(img,0)      #0 for vertical flip
    horizontalFlip = cv2.flip(img,1)      #positive for vertical flip
    
    show(verticalFlip)
    show(horizontalFlip)

    # flip(img)





