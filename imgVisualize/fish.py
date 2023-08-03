import cv2


# class ball:

    
#     def __init__(self,canvas,x,y,d,xvelo,yvelo,color):
#         self.canvas=canvas
#         self.image=canvas.create_oval(x,y,d,d,fill=color)
#         self.xvelo=xvelo
#         self.yvelo=yvelo


#     def move(self):
#         coord = self.canvas.coords(self.image)
#         print(coord)

#         if(coord[2]>=(self.canvas.winfo_width()) or coord[0]<0):
#             self.xvelo=self.xvelo*-1
        
#         if(coord[3]>=(self.canvas.winfo_width()) or coord[1]<0):
#             self.yvelo=self.yvelo*-1

#         self.canvas.move(self.image,self.xvelo,self.yvelo)


# left to right
class Fish():
    def __init__(self, canvas,x,y,xVelo, yVelo, photo):
        self.canvas = canvas
        self.img = canvas.create_image(x,y, image=photo)
        self.xVelo = xVelo
        self.yVelo = yVelo

    def move(self):
        coord = self.canvas.coords(self.img)
        print(coord)

        if(coord[0]>=(self.canvas.winfo_width() or coord[0]<=0)):
            
            self.xVelo=self.xVelo*-1

        if(coord[0]<0):
            self.xVelo=self.xVelo*-1
        
        if(coord[1]>=(self.canvas.winfo_width())):
            self.yVelo=self.yVelo*-1
        
        if(coord[1]<0):
            self.yVelo=self.yVelo*-1

        self.canvas.move(self.img,self.xVelo,self.yVelo)

    # func to flip image
    def flipimg(raw_img):
        image = cv2.imread(raw_img)

        # Check if the image is loaded successfully
        if image is None:
            print("Error: Unable to load the image.(flipimg)")
            return
        
        # Flip the image horizontally
        flipped_image = cv2.flip(image, 1)

        # Save the flipped image to the specified output path
        cv2.imwrite(image, flipped_image)