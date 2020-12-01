#import python3 print function
from __future__ import print_function

#import required modules
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math
import pprint

#program parameters
k = 200             #number of iterations
d = 1               #defined step length; not used as variable as all steps are unit vectors (have inherent length = 1)
pointsList = []     #blank list to hold point data; has form ['point name', point coordinates, 'parent point']
segmentsList = []   #blank list to hold line segment endpoint coordinates

#define distance calculation function
def calcDist(x,y):
    dist = math.sqrt((x)**2+(y)**2)
    return dist

#create start point
startX = 50         #x coordinate
startY = 50         #y coordinate
startName = 'q0'    #name
startData = [startName,(startX,startY)] #pointsList data entry
pointsList.append(startData)

#find closest node
for i in range(1,k+1):
    #name of point being determined
    pointName = "q{}".format(i)
    #coordinates of random point
    randomX = np.random.randint(0,101)
    randomY = np.random.randint(0,101)
    #blank list to hold point-to-point distances; clears each iteration
    distances = []

    #calculate distance from random point to each node
    for j in range(len(pointsList)):
        #coordinate distances between random point and each successive node
        distX = randomX-pointsList[j][1][0]
        distY = randomY-pointsList[j][1][1]
        #calculate normalized distance from random point to node ("node distance")
        distance = calcDist(distX,distY)
        #add individual node distance to list of node distances
        distances.append(distance)

    #determine parent point - the node to which the random point is closest
    #very closely taken from: https://thispointer.com/numpy-amin-find-minimum-value-in-numpy-array-and-its-index/
    closestIndex = int(np.where(distances == np.amin(distances))[0])

    #determine/define coordinates of parent point
    parentCoords = (pointsList[closestIndex][1][0],pointsList[closestIndex][1][1])

    #create vector from closest point to random point
    closestVector = [distX,distY]

    #calculate unit vector
    unitVector = [dist/distance for dist in closestVector]

    #create parent point data entry
    parent = "q{}".format(closestIndex)

    #determine coordinates of new node
    pointX = pointsList[closestIndex][1][0] + unitVector[0]
    pointY = pointsList[closestIndex][1][1] + unitVector[1]
    pointCoords = (pointX,pointY)

    #create data entry for most recent point
    pointData = [pointName,pointCoords,parent]

    #add most recent point data to point data list
    pointsList.append(pointData)

    #create line segment endpoints list entry
    endpoints = [(parentCoords),(pointCoords)]

    #add endpoints list entry to line segment data list
    segmentsList.append(endpoints)

#print line segment data list
# pprint.pprint(segmentsList)

#print point data in an aesthetically pleasing manner
# pprint.pprint(pointsList)

#generate x- and y-values for scatter plot
pointsX = [pointsList[i][1][0] for i in range(len(pointsList))]
pointsY = [pointsList[i][1][1] for i in range(len(pointsList))]

#generate subplots to allow scatter and line plots on same figure with same axes
fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
#create scatter plot
fig = plt.scatter(pointsX,pointsY)
#add line segments
lineSegments = mpl.collections.LineCollection(segmentsList)
ax.add_collection(lineSegments)

#show RRT plot
plt.show()
