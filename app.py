import numpy as np
from Functions.ToSkeleton.app import PointsFromImage,ToSkeleton
from Functions.Merge.app import merge_close_lines
import cv2
import os

Images=(os.listdir(os.path.join('Images',"Input")))

for Img in Images:
    image=cv2.imread(os.path.join('Images','Input',Img))
    image=ToSkeleton(image)
    PFromImg,Lines=PointsFromImage(image)


    
    Canvas=np.zeros((image.shape[0],image.shape[1],3),np.uint8)
    for Point in Lines:
        x1, y1, x2, y2 = Point[0]
        cv2.line(Canvas,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.circle(Canvas,(x1,y1),10,(0,255,0),2)
        cv2.circle(Canvas,(x2,y2),10,(0,0,255),2)
    cv2.imwrite(f'Images/Output/{Img}',Canvas)
    LinesMerged=merge_close_lines(Lines,40)
    
    Canvas=np.zeros((image.shape[0],image.shape[1],3),np.uint8)
    for Point in LinesMerged:
        x1, y1, x2, y2 = Point[0]
        cv2.line(Canvas,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.circle(Canvas,(x1,y1),10,(0,255,0),2)
        cv2.circle(Canvas,(x2,y2),10,(0,0,255),2)

    cv2.imwrite(f'Images/Output/Merged{Img}',Canvas)