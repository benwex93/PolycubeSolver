import numpy as np
import math
# from scipy import ndimage
from PIL import Image
import matplotlib.pyplot as plt
import imageio
import cv2

#  inputs
img = cv2.imread("head.png")
rotation_amount_degree = 45

#  convert rotation amount to radian
rotation_amount_rad = rotation_amount_degree * np.pi / 180.0


#  get dimension info
height, width, num_channels = img.shape


#  create output image, for worst case size (45 degree)
max_len = int(math.sqrt(height*height + width*width))
rotated_image = np.zeros((max_len, max_len, num_channels))
#rotated_image = np.zeros((img.shape))


rotated_height, rotated_width, _ = rotated_image.shape
mid_row = int( (rotated_height+1)/2 )
mid_col = int( (rotated_width+1)/2 )

#  for each pixel in output image, find which pixel
#it corresponds to in the input image
for r in range(rotated_height):
    for c in range(rotated_width):
        #  apply rotation matrix, the other way
        y = (r-mid_col)*math.cos(rotation_amount_rad) + (c-mid_row)*math.sin(rotation_amount_rad)
        x = -(r-mid_col)*math.sin(rotation_amount_rad) + (c-mid_row)*math.cos(rotation_amount_rad)

        #  add offset
        y += mid_col
        x += mid_row

        #  get nearest index
        #a better way is linear interpolation
        x = round(x)
        y = round(y)

        #print(r, " ", c, " corresponds to-> " , y, " ", x)

        #  check if x/y corresponds to a valid pixel in input image
        if (x >= 0 and y >= 0 and x < width and y < height):
            rotated_image[r][c][:] = img[y][x][:]


#  save output image
output_image = Image.fromarray(rotated_image.astype("uint8"))
output_image.save("rotated_image.png")