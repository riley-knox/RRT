#import python3 print function
from __future__ import print_function

#import required modules
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math
import pprint

#program parameters
k = 50              #number of iterations - MAY NOT BE NECESSARY
d = 1               #defined step length; not used as variable as all steps are unit vectors (have inherent length = 1)
pointsList = []     #blank list to hold point data; has form ['point name', point coordinates, 'parent point']
segmentsList = []   #blank list to hold line segment endpoint coordinates
obstaclesList = []  #blank list to hold obstacle coordinates and radii
clearPath = False   #initial condition for straight-line path to end point

#fix random seed
np.random.seed(707023546)

#define distance calculation function
def calcDist(x1,x2,y1,y2):
    dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return dist

#define function to check if a point is inside an obstacle
def isinObstacle(x,y):
    distList = []      #empty list to hold distances to each obstacle center
    inObstacles = []    #empty list for strings indicating intersection condition with each obstacle
    for i in range(len(obstaclesList)):
        obDist = calcDist(x,obstaclesList[i][0][0],y,obstaclesList[i][0][1]) #calculate distance to each obstacle center
        #print('distance to obstacle {}: '.format(i+1), obDist) - #DELETE ONCE EVERYTHING WORKING
        distList.append(obDist)     #add distance to obstacle i to list of distances - CAN PROBABLY DELETE
        if obDist <= obstaclesList[i][1]:       #check if distance to center of obstacle i is less than radius of obstacle i
            #print('Point within obstacle {}!'.format(i+1)) - #DELETE ONCE EVERYTHING WORKING
            condition = True        #mark point as within obstacle i
        else:
            condition = False       #mark point as missing obstacle i
        inObstacles.append(condition)       #add collision condition to
    #print(inObstacles)
    return inObstacles

#define function to find equation of a line between two points
#two points used will be most recently added node and end point
def lineEquation((x1,y1),(x2,y2)):
    A = y1 - y2
    B = x2 - x1
    C = (x1*y2) - (x2*y1)
    return (A,B,C)

#define function to calculate distance from a point to a line
#inputs will be coefficients returned from lineEquation function and center coordinates of obstacle
def pointtoLine((A,B,C),(x,y)):
    disttoLine = abs(((A*x) + (B*y) + C))/(math.sqrt(A**2 + B**2))
    return disttoLine

#define function to check if there is a clear path to the endpoint
#def isPathClear():
#    pathDists = []          #empty list to hold distances from center of each obstacle to path from newest node to endpoint
#    pathinObstacles = []    #empty list for strings indicating if path to endpoint intersects with each obstacle
#    for i in range(len(obstaclesList)):


#generate obstacles
#number of obstacles
N = 20
#x- and y-coordinates of obstacles on 0-100 scale
x = 100*np.random.rand(N)
y = 100*np.random.rand(N)
centers = [(x,y) for x,y in zip(x,y)]       #create list of obstacle centers
#obstacle sizes
radii = (10*np.random.rand(N))
#make list of obstacle properties
for i in range(N):
   obstacleCenter = centers[i]
   obstacleRadius = radii[i]
   obstacleProps = (obstacleCenter,obstacleRadius)
   obstaclesList.append(obstacleProps)
pprint.pprint(obstaclesList) #print list of obstacle coordinates & radii - CAN DELETE IF EVERYTHING IS WORKING

#start point creation
#generate coordinates and check for obstacle collision; re-generate if collision occurs
while True:
    #create start point in range 10-30 on both axes
    startX = 10 + 20*np.random.rand()               #x coordinate
    startY = 10 + 20*np.random.rand()               #y coordinate
    #print('starting coordinates: ',(startX,startY))     #CAN DELETE ONCE WORKING
    startCollisions = isinObstacle(startX,startY)   #establish collision case for each obstacle
    startYesorNo = any(startCollisions)             #check if collision exists
    #print(startYesorNo)                #CAN DELETE ONCE WORKING
    if startYesorNo == True:            #re-run coordinate generation if collision exists
        pass
    else:                               #break loop if no collision
        break
#print('start: ',(startX,startY))       #print start coordinates - CAN DELETE
startColor = '#1ca120'                  #start point color
startName = 'q0'                        #name
startData = [startName,(startX,startY)] #pointsList data entry
pointsList.append(startData)            #add start point data to points data list

#end point creation
while True:
    #create end point in range 70-90 on both axes
    endX = 70 + 20*np.random.rand()                 #x coordinate
    endY = 70 + 20*np.random.rand()                 #y coordinate
    print('end coordinates: ',(endX,endY))
    endCollisions = isinObstacle(endX,endY)         #establish collision case for each obstacle
    endYesorNo = any(endCollisions)                 #check if collision exists
    #print(endYesorNo)                  #CAN DELETE ONCE WORKING
    if endYesorNo == True:              #re-run generation if collision exists
        pass
    else:                               #break loop if no collision
        break
#print('end: ',(endX,endY))              #print end coordinate - CAN DELETE
endColor = '#ff9b00'

#make sure start and end points are not inside an obstacle
#startCollisions = isinObstacle(startX,startY)       #check start point first
#print(startCollisions)                             #print intersection condition with each obstacle - CAN DELETE
#print(any(startCollisions))                         #print whether point has a collision - CAN DELETE
#endCollisions = isinObstacle(endX,endY)             #check end point second
#print(endCollisions)                               #end point intersection conditions - CAN DELETE
#print(any(endCollisions))                           #print whether point has a collision - CAN DELETE

#add new points to tree until there is a clear path to the end point
while clearPath == False:
    #generate new nodes, checking for collisions with obstacles
    while True:
        pointName = "q{}".format(len(pointsList))
        #print(len(pointsList))              #name of point being added - CAN DELETE ONCE WORKING
        #print(pointName)
        #coordinates of random point
        randomX = np.random.randint(0,101)
        randomY = np.random.randint(0,101)
        #print('random point: ',(randomX,randomY))
        #blank list to hold point-to-point distances; clears each iteration
        distances = []

        #calculate distance from random point to each node
        for i in range(len(pointsList)):
            #calculate normalized distance from random point to node ("node distance")
            distance = calcDist(pointsList[i][1][0],randomX,pointsList[i][1][1],randomY)
            #print('distance to point {} = '.format(pointsList[i][0]),distance)
            #add individual node distance to list of node distances
            distances.append(distance)

        #determine parent point - the node to which the random point is closest
        #very closely taken from: https://thispointer.com/numpy-amin-find-minimum-value-in-numpy-array-and-its-index/
        closestIndex = int(np.where(distances == np.amin(distances))[0])
        #print(closestIndex)            #CAN DELETE

        #determine/define coordinates of parent point
        parentCoords = (pointsList[closestIndex][1][0],pointsList[closestIndex][1][1])
        #print('parent point: {}; coordinates: {}'.format(pointsList[closestIndex][0],(pointsList[closestIndex][1][0],pointsList[closestIndex][1][1])))      #print parent point & its coordinates - CAN DELETE ONCE WORKING

        #create vector from closest point to random point
        distX = randomX - pointsList[closestIndex][1][0]
        distY = randomY - pointsList[closestIndex][1][1]
        closestVector = [distX,distY]
        #print('vector to closest point: ',closestVector)

        #calculate unit vector
        unitVector = [dist/distance for dist in closestVector]
        #print('unit vector: ',unitVector)

        #create parent point data entry
        parent = "q{}".format(closestIndex)

        #determine coordinates of new node
        pointX = pointsList[closestIndex][1][0] + unitVector[0]
        pointY = pointsList[closestIndex][1][1] + unitVector[1]
        pointCoords = (pointX,pointY)
        print('new point: ',pointCoords)

        #determine if new point is in an obstacle
        pointCollisions = isinObstacle(pointCoords[0],pointCoords[1])
        pointYesorNo = any(pointCollisions)
        if pointYesorNo == True:
            pass
        else:
            break

    #create data entry for most recent point
    pointData = [pointName,pointCoords,parent]
    #print('new point: ',pointData)

    #add most recent point data to point data list
    pointsList.append(pointData)
    #print('list of points:',pointsList)

    #create line segment endpoints list entry
    endpoints = [parentCoords,pointCoords]

    #add endpoints list entry to line segment data list
    segmentsList.append(endpoints)

    #calculate line equation between added node and end point
    lineCoefficients = lineEquation(pointCoords,(endX,endY))
    print('A, B, C: ',lineCoefficients)

    #calculate distances from obstacle centers to node-end point line
    intersectConditions = []     #empty list to hold strings indicating intersection condition with each obstacle
    obstaclestoLine = []         #empty list to hold distances from obstacles to line
    for i in range(len(obstaclesList)):
        obstacleDistance = pointtoLine(lineCoefficients,obstaclesList[i][0])
        obstaclestoLine.append(obstacleDistance)        #CAN PROBABLY DELETE
        if obstacleDistance <= obstaclesList[i][1]:
            condition = True
        else:
            condition = False
        intersectConditions.append(condition)
    print(obstaclestoLine)
    print(intersectConditions)

    #check if obstacle-to-line distances are less than obstacle radii




    break

#create subplots
fig, ax = plt.subplots(nrows = 1, ncols = 1, sharex = True, sharey = True)
#create obstacles as a collection of circular patches
obstacles = [plt.Circle(center, radius) for center,radius in zip(centers,radii)]
patches = mpl.collections.PatchCollection(obstacles, facecolors = 'black')
ax.add_collection(patches)
#plot start and end points
plt.scatter(startX,startY,c=startColor,marker='x')
plt.scatter(endX,endY,c=endColor,marker='+')
#set title
ax.set_title('RRT with Obstacles')
#set axis limits
plt.xlim(0,100)
plt.ylim(0,100)
#set title
plt.show()
