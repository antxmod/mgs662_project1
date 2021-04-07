import pandas as pd
import numpy as np
from skimage.transform import resize

import matplotlib.pyplot as plt
import os,glob
import re
import csv
#matplotlib inline
from skimage.io import imread, imshow

paths = [os.getcwd()+"\pics"]
arrays = {}

for path in paths:
    for img_file in glob.glob(os.path.join(path, '*.jpg')):
        print(img_file)
        image = imread(img_file, as_gray=False)
        imshow(image)
        image.shape
        np.array(image)
        img_resized = resize(image, (5,5))
        image_array = np.array(img_resized)
        print(image_array[0],image_array[1],image_array[3])
        arrays[os.path.split(img_file)[1]] = (image_array[0],image_array[1],image_array[2])
df=pd.DataFrame.from_dict(arrays)
print(df)
df.to_csv('export.csv')        


        
