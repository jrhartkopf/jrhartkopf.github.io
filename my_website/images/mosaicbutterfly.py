# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFilter
import PIL
from PIL import ImageOps
import matplotlib.pyplot as plt
import os.path
import numpy as np # “as” lets us use standard abbreviations

backgroundColor = (0,)*3
pixelSize = 9

image = Image.open('monarchj.jpg')
image = image.resize((image.size[0]/pixelSize, image.size[1]/pixelSize), Image.NEAREST)
image = image.resize((image.size[0]*pixelSize, image.size[1]*pixelSize), Image.NEAREST)
pixel = image.load()

for i in range(0,image.size[0],pixelSize):
  for j in range(0,image.size[1],pixelSize):
    for r in range(pixelSize):
      pixel[i+r,j] = backgroundColor
      pixel[i,j+r] = backgroundColor

image.save('output.png')

image = image.filter(ImageFilter.BLUR)
image.save('monarchblur.png')
image=Image.open('monarchj.jpg')
inverted_image= PIL.ImageOps.invert(image)
inverted_image.save('invertedmonarch.png')
   
'''Read the image data'''
   # Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
  # Build an absolute filename from directory + filename
filename = os.path.join(directory, 'invertedbutterfly.png')
filename2 = os.path.join(directory,'invertedmonarch.png')
filename1 = os.path.join(directory,'redyellowblur.png')
filename3 = os.path.join(directory,'output.png')
filename4 = os.path.join(directory,'pinkoutput.png')
  # Read the image data into an array
img = plt.imread(filename)
img1 = plt.imread(filename1)
img2 = plt.imread(filename2)
img3 = plt.imread(filename3)
img4 = plt.imread(filename4)
'''Show the image data'''
# Create figure with 1 subplot
# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1,5)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img1, interpolation='none')
ax[2].imshow(img2, interpolation='none')
ax[3].imshow(img3, interpolation='none')
ax[4].imshow(img4, interpolation='none')
# Show the figure on the screen
fig.show()