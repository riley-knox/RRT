#import python3 print function
from __future__ import print_function

#import required modules
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import imageio
import math

#program parameters
k = 5               #number of iterations
d = 1               #step length
pointsList = []     #blank list to hold point data

#define distance calculation function
def calcDist(x,y):
    dist = math.sqrt((x)**2+(y)**2)
    return dist

#create start point
startX = 50         #x coordinate
startY = 50         #y coordinate
startName = 'q0'    #name
startData = [startName,(startX,startY)]
pointsList.append(startData)

#find closest node
for i in range(1,k+1):
    pointName = "q{}".format(i)            #name of point being determined
    print(pointName)       #CAN DELETE ONCE LOOP WORKS
    randomX = np.random.randint(0,101)      #coordinates of random point
    randomY = np.random.randint(0,101)
    print("coordinates of random point: ",randomX,randomY)  #CAN DELETE ONCE LOOP WORKS
    distances = []                      #blank list to hold point-to-point distances; clears each iteration
    for j in range(len(pointsList)):
        distX = randomX-pointsList[j][1][0]
        distY = randomY-pointsList[j][1][1]
        print("coordinate distances from point{}: ".format(j),distX,distY)  #CAN DELETE ONCE LOOP WORKS
        distance = calcDist(distX,distY)
        distances.append(distance)
    print("point-to-point distances: ",distances)        #CAN DELETE ONCE LOOP WORKS
    closestIndex = int(np.where(distances == np.amin(distances))[0])     #very closely taken from: https://thispointer.com/numpy-amin-find-minimum-value-in-numpy-array-and-its-index/
    print("index of closest point: ",closestIndex)     #CAN DELETE ONCE LOOP WORKS
    closestVector = [distX,distY]           #vector from closest point to random point
    print("vector from closest point: ",closestVector)    #CAN DELETE ONCE LOOP WORKS
    unitVector = [dist/distance for dist in closestVector]
    print("unit vector: ",unitVector)       #CAN DELETE ONCE LOOP WORKS
    print("closest point + coordinates: ",pointsList[closestIndex])
    parent = "q{}".format(closestIndex)
    print("parent point: ",parent)
    pointX = pointsList[closestIndex][1][0] + unitVector[0]
    pointY = pointsList[closestIndex][1][1] + unitVector[1]
    pointCoords = (pointX,pointY)
    print("new point coordinates: ",pointCoords)      #CAN DELETE ONCE LOOP WORKS
    pointData = [pointName,pointCoords]   #CHANGE TO COORDINATES OF ADDED POINT, NOT RANDOM
    pointsList.append(pointData)
print("point list: ",pointsList)

#scatter plot of points
pointsX = [pointsList[i][1][0] for i in range(len(pointsList))]
pointsY = [pointsList[i][1][1] for i in range(len(pointsList))]
plt.scatter(pointsX,pointsY)
plt.show()
