import cv2
import numpy as np

def PointsFromImage(image):
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    lines_list = []
    lines = cv2.HoughLinesP(edges,1,np.pi/180,threshold=100,minLineLength=5,maxLineGap=10)

                

    # for points in lines:
    #     x1, y1, x2, y2 = points[0]
    #     radius = 4
    #     # cv2.ellipse(image, (x1, y1), (radius, radius), 0, 0, 360, (0, 0, 255), 1)
    #     # cv2.ellipse(image, (x2, y2), (radius, radius), 0, 0, 360, (0, 0, 255), 1)
    #     # lines_list.append([(x1, y1), (x2, y2)])
    return(image,lines)


threshold=10

image=cv2.imread('I.png')
Lines=PointsFromImage(image)[1]
# LinesCopy=Lines
# Delete=np.array(Lines.shape)
# for i,Point in enumerate(Lines):
#     VertX1,VertY1,VertX2,VertY2=Point[0]
#     for j,Points2 in enumerate(LinesCopy):
#         Vert2X1,Vert2Y1,Vert2X2,Vert2Y2=Points2[0]
#         print(f'{Point[0]},{Points2[0]}')
#         if abs(VertX1-Vert2X1) <threshold and abs(VertY1-Vert2Y1) <threshold:
#             # print(j)
#             Delete=np.append(Delete,Points2)
#             # print(LinesCopy.shape)
#             print('Delete')
#             break
#         break
for line in Lines:
    # cv2.line(image,(line[0][0],line[0][1]),(line[0][2],line[0][3]),(0,255,0),2)

    print(line)
    
cv2.imwrite('f2.jpg',image)           

def merge_close_lines(coordinates, threshold):
    merged_lines = []
    merged_indices = set()

    for i in range(len(coordinates)):
        if i in merged_indices:
            continue

        line = coordinates[i].reshape(1, 4)
        merged_line = line

        for j in range(i + 1, len(coordinates)):
            if j in merged_indices:
                continue

            other_line = coordinates[j].reshape(1, 4)
            dist = np.sqrt((line[0, 0] - other_line[0, 0]) ** 2 + (line[0, 1] - other_line[0, 1]) ** 2)

            if dist <= threshold:
                merged_line = np.vstack((merged_line, other_line))
                merged_indices.add(j)
                print('Merged')
        merged_lines.append(merged_line)

    return merged_lines


coordinates = Lines
threshold = 50
merged_lines = merge_close_lines(coordinates, threshold)

# print("Merged lines:")

for line in merged_lines:
    cv2.line(image,(line[0][0],line[0][1]),(line[0][2],line[0][3]),(0,255,0),2)

    print(line)
    
cv2.imwrite('f.jpg',image)