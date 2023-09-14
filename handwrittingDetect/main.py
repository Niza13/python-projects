# handwritten numbers and characters detection 

import tensorflow as tf     #pip install tenserflow
import matplotlib.pyplot as plt     #to plot images
import numpy as np  #for resizing img
import cv2          #pip install opencv-python  for img
import os

# to create neural network model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D

print(len(tf.config.list_physical_devices('GPU')))      #using gpu for speed

mnist = tf.keras.datasets.mnist     #calling dataset
# tensorflow already consist of mnist(handwritten dataset of 0-9 images) dataset which can be loaded using keras so no need to download


# dividing dataset in tarin and test groups
(x_train,y_train),(x_test,y_test) = mnist.load_data()


# plt.imshow(x_train[0])
# plt.show()                it'll print colored img if there

# to show in b/w
plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.show()

# before normalizing values
print(x_train[0])


# normalizing data so value comes instead between from 0-255 to 0-1 only 
x_train = tf.keras.utils.normalize(x_train,axis=1)
x_test = tf.keras.utils.normalize(x_test,axis=1)
# display after normalizing
plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.show()

# after normalizing
print(x_train[0])   #x_train has data
print(y_train[0])   #y_train has label


# resizing image for convolutional operation (extending a dimension)
img_size =28

x_trainr = np.array(x_train).reshape(-1,img_size,img_size,1)        #-1 corresponds to 60000,28x28 is img size and 1 is extended dimension
x_testr = np.array(x_test).reshape(-1,img_size,img_size,1)          #-1 corresponds to 10000,28x28 is img size and 1 is extended dimension

print('training data dimension', x_trainr.shape)
print('testing data dimension', x_testr.shape)


# creating deep learning architecture
model = Sequential()        #means we're going to concatenate all our imported layers sequentially


# 1st layer
model.add(Conv2D(64,(3,3), input_shape = x_trainr.shape[1:]))   #only for 1st convolution layer to mention input  layer size (64 layers and 3x3 size)   (result=28-3+1=26) 
model.add(Activation("relu"))   #activation function to make it non-linear (value>0 then ok else will drop value)
model.add(MaxPooling2D(pool_size=(2,2)))    #maxpooling


# 2nd layer
model.add(Conv2D(64,(3,3), input_shape = x_trainr.shape[1:]))   #only for 1st convolution layer to mention input  layer size (64 layers and 3x3 size) (result=26-3+1=24)
model.add(Activation("relu"))   #activation function to make it non-linear (value>0 then ok else will drop value)
model.add(MaxPooling2D(pool_size=(2,2)))    #maxpooling


# 3rd layer
model.add(Conv2D(64,(3,3), input_shape = x_trainr.shape[1:]))   #only for 1st convolution layer to mention input  layer size (64 layers and 3x3 size) (result=24-3+1=22)
model.add(Activation("relu"))   #activation function to make it non-linear (value>0 then ok else will drop value)
model.add(MaxPooling2D(pool_size=(2,2)))    #maxpooling


# after 3 layers now have fully connected layer after flatten(2d to 1d) 
model.add(Flatten())

# fully connected layer 1
model.add(Dense(64))    
model.add(Activation("relu"))  

# fully connected layer 2
model.add(Dense(32))        #to half dense and to reach 10    
model.add(Activation("relu"))  

# last fully connected layer (it must be equal to 10)
model.add(Dense(10))    
model.add(Activation("softmax"))    #last activation func must be softmax or (sigmoid-->if binary classification and one neuron in dense(1)) (class probabilities)
# we've multiple class-->dense(10) so softmax
  

model.summary()     #to check all over model


# model compilation 
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=['accuracy'])

# fitting data in model
model.fit(x_trainr,y_train, epochs=3, validation_split=0.3) #training model


# checking on test data now
test_loss, test_accu = model.evaluate(x_testr,y_test)
print('loss: ',test_loss)
print('accu: ',test_accu)


# getting image from system
img = cv2.imread('6.jpeg', cv2.IMREAD_UNCHANGED)
gray = cv2.cvtColor(img,cv2.COLOR_BayerGR2GRAY)
resized = cv2.resize(gray,(28,28), interpolation=cv2.INTER_AREA)

# normalizing image
newimg = tf.keras.utils.normalize(resized,axis=1)   #between 0-1
