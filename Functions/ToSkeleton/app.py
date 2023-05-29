from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert
import cv2
import numpy as np

image=cv2.imread('Input.jpg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

height=image.shape[0]
width=image.shape[1]
Ratio=height/540


image=cv2.resize(image,(int(width/Ratio),int(height/Ratio)))
OgImage=cv2.resize(image,(int(width/Ratio),int(height/Ratio)))

OgImage=image
image=invert(image)

skeleton = skeletonize(image)

skeleton=np.array(skeleton)
skeleton=cv2.cvtColor(skeleton,cv2.COLOR_RGB2GRAY)


skeleton=invert(skeleton)
image=invert(image)
cv2.imwrite('Output.jpg',skeleton)
