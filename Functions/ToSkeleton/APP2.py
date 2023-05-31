import cv2
import numpy as np

# Read image
image = cv2.imread('I.png')
image2 = cv2.imread('Output.jpg')


def PointsFromImage(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines_list = []
    lines = cv2.HoughLinesP(edges,1,np.pi/180,threshold=100,minLineLength=5,maxLineGap=10)
    for points in lines:
        x1, y1, x2, y2 = points[0]
        radius = 4
        cv2.ellipse(image, (x1, y1), (radius, radius), 0, 0, 360, (0, 0, 255), 1)
        cv2.ellipse(image, (x2, y2), (radius, radius), 0, 0, 360, (0, 0, 255), 1)
        lines_list.append([(x1, y1), (x2, y2)])
    return(image,lines)

print()

cv2.imwrite('detectedLines1.png', PointsFromImage(image)[0])
cv2.imwrite('detectedLines2.png', PointsFromImage(image2)[0])
