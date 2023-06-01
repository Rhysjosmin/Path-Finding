import cv2
import numpy as np
from Functions.ToSkeleton.app import *


Image=cv2.imread('Images/Input/E.png')
# Image=cv2.resize(Image,(64,64))
Image=ToSkeleton(Image)

PFromImg,Lines=PointsFromImage2(Image)
# print(Lines)

    
Canvas=np.zeros((Image.shape[0],Image.shape[1],3),np.uint8)
for Point in Lines:
    x1, y1, x2, y2 = Point[0]
    cv2.line(Canvas,(x1,y1),(x2,y2),(0,255,0),1)
    # cv2.circle(Canvas,(x1,y1),1,(0,255,0),1)
    # cv2.circle(Canvas,(x2,y2),1,(0,0,255),1)
cv2.imwrite(f'Images/Output/Op.png',Canvas)
cv2.imwrite(f'Images/Output/Op_Sk.png',Image)


