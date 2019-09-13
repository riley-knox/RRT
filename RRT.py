#import python3 print function
from __future__ import print_function

#import required modules
import matplotlib as mpl
import numpy as np
import imageio
import math

#program parameters
k = 2               #number of iterations
d = 1               #step length
pointsList = []    #blank list to hold point data
distances = []      #blank list to hold point-to-point distances

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
    print(randomX,randomY)  #CAN DELETE ONCE LOOP WORKS
    for j in range(len(pointsList)):
        distX = abs(randomX-pointsList[j][1][0])
        distY = abs(randomY-pointsList[j][1][1])
        #print(distX,distY)  #CAN DELETE ONCE LOOP WORKS
        distance = calcDist(distX,distY)
        distances.append(distance)
    print(distances)        #CAN DELETE ONCE LOOP WORKS
    closestIndex = np.where(distances == np.amin(distances))[0]     #very closely taken from: https://thispointer.com/numpy-amin-find-minimum-value-in-numpy-array-and-its-index/
    print(closestIndex)     #CAN DELETE ONCE LOOP WORKS

    pointData = [pointName,(randomX,randomY)]   #CHANGE TO COORDINATES OF ADDED POINT, NOT RANDOM
    pointsList.append(pointData)
print(pointsList)
