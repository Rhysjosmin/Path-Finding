import random
from skimage.morphology import skeletonize
from skimage.util import invert
import cv2
import numpy as np
from PIL import ImageDraw,Image
ogWidth=0
ogHeight=0
def ToSkeleton(image):
    global ogWidth,ogHeight
    # image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    # print(image)
    # print('----')
    height=image.shape[0]
    width=image.shape[1]
    ogWidth=width
    ogHeight=height
    Ratio=height/64
    image=cv2.resize(image,(int(width/Ratio),int(height/Ratio)))
    

    
 

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
    cv2.imwrite('edges.jpg',edges)
    lines = cv2.HoughLinesP(edges,1,np.pi/180,threshold=10,minLineLength=0,maxLineGap=1)



    # for points in lines:
    #     x1, y1, x2, y2 = points[0]
    #     radius = 4
    #     cv2.ellipse(image, (x1, y1), (radius, radius), 0, 0, 360, (0, 0, 255), 1)
    #     cv2.ellipse(image, (x2, y2), (radius, radius), 0, 0, 360, (0, 0, 255), 1)
    #     lines_list.append([(x1, y1), (x2, y2)])
    return(image,lines)


def PointsFromImage2(image):
    i2=np.copy(image)
    
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    lines_list = []
    NewLines = []
    Done = []
    dest = cv2.cornerHarris(image, 2, 5, 0.07)
    lines = cv2.HoughLinesP(edges,1,np.pi/180,threshold=10,minLineLength=0,maxLineGap=1)
    for _ in range(1):
        for r,row in enumerate(image):
            for c,element in enumerate(row):
                if element<255:
                    i2[r][c]=0
                    if((image[r+1][c])<255  and (image[r-1][c]>=255)) or (((image[r][c+1])<255)  and (image[r][c-1]>=255)) or(image[r+1][c]>255 and (image[r][c+1]>255) and (image[r][c-1]>255)):
                        i2[r][c]=0
                        lines_list.append([c,r])
                        
                    else:
                        i2[r][c]=255                       
                else:
                    pass
    
    ListOfPoints=np.copy(lines_list)
    MaxDist=4
    print(NewLines)
    i=-1
    for points_i,points_v in enumerate(ListOfPoints):
        j=-1
        points=ListOfPoints[i]
        # cv2.circle(image,(points[0],points[1]),1,(0,255,0),1)
        for other_i,other_v in enumerate(ListOfPoints):
            print(j)
            j+=1
            other=ListOfPoints[j]
            if [points[0],points[1]] in Done:
                break
            else:
                if((abs(points[0]-other[0]))<MaxDist) and ((abs(points[1]-other[1]))<MaxDist):
                    c=int(np.floor((points[0]+other[0])/2))
                    r=int(np.floor((points[1]+other[1])/2))
                    NewLines.append([points[0],points[1]])
                    Done.append([points[0],points[1]])
                    Done.append([other[0],other[1]])
                if(i==j):
                    break
          
            
                
        i+=1
          


    print((NewLines))
    print('----')
    print((lines_list))
    # i2=cv2.resize(np.ones((ogWidth,ogHeight)),(ogWidth,ogHeight),interpolation=cv2.INTER_NEAREST)
    i2=cv2.resize(image,(ogWidth,ogHeight),interpolation=cv2.INTER_NEAREST)
    RatioW=int(ogHeight/ogWidth)*30
    RatioH=int(ogHeight/ogWidth)*30
    # f=10
    Chosen=[]
    for points in NewLines:
        cv2.circle(i2,(points[0]*RatioH,points[1]*RatioW),20,(0,255,0),1)
        for p2 in NewLines: 
            if(random.random()<random.random()):
                cv2.line(i2,(points[0]*RatioH,points[1]*RatioW),(p2[0]*RatioH,p2[1]*RatioW),(0,255,0),1)
                Chosen.append([points[0]*RatioH,points[1]*RatioW])
                Chosen.append([p2[0]*RatioH,p2[1]*RatioW])
  
    # cv2.imwrite('imTex.png',i2)
    return(i2,Chosen)



