# load and run model 


import tensorflow as tf     #pip install tenserflow
import matplotlib.pyplot as plt     #to plot images
import numpy as np  #for resizing img
import cv2          #pip install opencv-python  for img
import os



# loading the saved model
model = tf.keras.models.load_model('handwrittingDetection.model')
print('model loaded successfully')

# trying to read our images
img_num = 1

while os.path.isfile("E:\VSCode\Python\projects\python-project\handwrittingDetect\img\4.jpeg"):
      # getting img with only last channel and not colors
      img_try = cv2.imread(f"E:\VSCode\Python\projects\python-project\handwrittingDetect\img\4.jpeg")[:,:,0]
    #   img_try = np.invert(np.array([img_try]))


      prediction = model.predict(img_try)
      print(f"digit is {np.argmax(prediction)}")

    #   plt.imshow(img_try[0], cmap=plt.cm.binary)
      plt.imshow(img_try, cmap=plt.cm.binary)


      plt.show()

    #   print("error")
    #   img_num +=1