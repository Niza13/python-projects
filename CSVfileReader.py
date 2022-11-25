# to read any csv files
import numpy as np
import os

print("enter name of file (with extension): ")
fname = input()


# it'll split the filename and store in list
split = os.path.splitext(fname)

# checking the valid extension
if(split[1]==".csv"):
    # to get csv file content
    read = np.loadtxt(fname,delimiter=",")
    
#     reading all columns and rows which exists
    print(read[:,:])
else:
        print("enter a csv file only")
