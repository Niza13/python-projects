from PIL import Image, ImageTk
from rembg import remove
import cv2



class Fish:

    def __init__(self, canvas,x,y,xVelo, yVelo, img):
        self.canvas = canvas
        # self.img = canvas.create_image(x,y, image=photo)
        self.xVelo = xVelo
        self.yVelo = yVelo
        self.img = img


    
    # convert func
    def convertImg(self):
        # opening and converting into RGB format
        im = Image.open(self.img)

        # Check if the image is loaded successfully
        if self.img is None:
            print("Error: Unable to load the image.(convertImg)")
            return
        
        rgb_im = im.convert('RGB')

        # to have a name
        name = self.img.split('.')
        name = name[0]+".png"
        # print(name)

        rgb_im.save(name)

        self.img = name



    # get resize image func
    def getImg(self):
        # getting image
        image = Image.open(self.img)
        # Resize the image using resize() method
        resize_image = image.resize((100, 100))

        # Save the resized image to a file
        # args is name of image
        resize_image.save(self.img)
    

    def photoImg(self):
        resized_image = Image.open(self.img)

        # converting to photo
        self.img = ImageTk.PhotoImage(resized_image)


    # bgRemove func
    def bgRemove(self):

        # getting image from name
        img = Image.open(self.img)
        
        # Check if the image is loaded successfully
        if img is None:
            print("Error: Unable to load the image.(bgRemove)")
            return

        # Removing the background from the given Image
        output = remove(img)

        #Saving the image in the given path
        output.save(self.img)


    def move(self):
        w=700
        h=600
        
        # getting image coords
        coords = self.canvas.coords(self.img)
        print(coords)

        # for width
        if(coords[0]>=(self.canvas.winfo_width()) or coords[0]<0):
            # flipping image
            # flipimg(ansImg)
            self.xVelo = self.xVelo*-1
        
        
        # for height
        if(coords[1]>=(self.canvas.winfo_height()) or coords[1]<0):
            self.yVelo = self.yVelo*-1

        

        self.canvas.move(self.img, self.xVelo, self.yVelo)
        
    

    


    # func to flip image
    def flipimg(img):
        image = cv2.imread(img)

        # Check if the image is loaded successfully
        if image is None:
            print("Error: Unable to load the image.(flipimg)")
            return
        
        # Flip the image horizontally
        flipped_image = cv2.flip(image, 1)

        # Save the flipped image to the specified output path
        cv2.imwrite(image, flipped_image)
        


