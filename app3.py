import numpy as np
from Functions.ToSkeleton.app import PointsFromImage2,ToSkeleton
from Functions.Merge.djikstras import dijkstra, graph
# from Functions.Merge.app import merge_close_lines
import cv2
import os

def process(image,vertexIndex):
    global graph
    image.name='Output'
    file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    height=image.shape[0]
    width=image.shape[1]
    image=ToSkeleton(image)
    image,lines=PointsFromImage2(image)
    print(len(lines))
    OPGraph=np.zeros((len(lines),len(lines)))
    for l,point in enumerate(lines):
        x,y=point
        for m,point2 in enumerate(lines):
            x1,y1=point2
            distance=np.power(np.power(x-x1,2)+np.power(y-y1,2),.5)   
            OPGraph[l][m]=distance
    
            # print(distance)
    print(OPGraph.shape)
    
    # print("Shortest path distances from vertex", 0, "to all other vertices:")
    # for i, distance in enumerate(0):
    #     print("Vertex", i, ":", distance)
        
    res=(dijkstra(OPGraph, vertexIndex))
    return image,res