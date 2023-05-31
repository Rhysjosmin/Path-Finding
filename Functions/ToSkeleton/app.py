from skimage.morphology import skeletonize
from skimage.util import invert
import cv2
import numpy as np

def ToSkeleton(image):
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    
    height=image.shape[0]
    width=image.shape[1]
    Ratio=height/1000
    image=cv2.resize(image,(int(width/Ratio),int(height/Ratio)))
    
    # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    # image = cv2.filter2D(image, -1, kernel)
    
 

    # cv2.imwrite('imageSharp.jpg',image)
    image=invert(image)
    skeleton = skeletonize(image)
    skeleton=np.array(skeleton)
    skeleton=cv2.cvtColor(skeleton,cv2.COLOR_RGB2GRAY)
    skeleton=invert(skeleton)
    return skeleton

def PointsFromImage(image):
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    lines_list = []
    lines = cv2.HoughLinesP(edges,1,np.pi/180,threshold=100,minLineLength=0,maxLineGap=10000)



    for points in lines:
        x1, y1, x2, y2 = points[0]
        radius = 4
        cv2.ellipse(image, (x1, y1), (radius, radius), 0, 0, 360, (0, 0, 255), 1)
        cv2.ellipse(image, (x2, y2), (radius, radius), 0, 0, 360, (0, 0, 255), 1)
        lines_list.append([(x1, y1), (x2, y2)])
    return(image,lines)


