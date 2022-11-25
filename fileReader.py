# to read csv or pkl files
import numpy as np
import os
import pickle
import json


print("enter name of file (with extension): ")
fname = input()

split = os.path.splitext(fname)

if(split[1]==".csv"):
    # to get csv file content
    read = np.loadtxt(fname,delimiter=",")
    print(read[:,:])

elif(split[1]==".pkl"):
    # to get content of pickle file
    read =  pickle.load(open(fname,"rb"))
    print(read)

elif(split[1]==".json"):
    # to get content of pickle file
    read =  json.load(open(fname,"r"))
    print(read)
else:
        print("enter a csv file only")
