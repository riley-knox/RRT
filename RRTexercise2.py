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

#fix random seed
#np.random.seed(34725534)

#define distance calculation function
def calcDist(x1,x2,y1,y2):
    dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return dist

#define function to check if a point IS inside an obstacle
def isinObstacle(x,y):
    distList = []      #empty list to hold distances to each obstacle center
    inObstacles = []    #empty list for strings indicating intersection condition with each obstacle
    for i in range(len(obstaclesList)):
        obDist = calcDist(x,obstaclesList[i][0][0],y,obstaclesList[i][0][1]) #calculate distance to each obstacle center
        #print('distance to obstacle {}: '.format(i+1), obDist) - #DELETE ONCE EVERYTHING WORKING
        distList.append(obDist)     #add distance to obstacle i to list of distances
        if obDist <= obstaclesList[i][1]:       #check if distance to center of obstacle i is less than radius of obstacle i
            #print('Point within obstacle {}!'.format(i+1)) - #DELETE ONCE EVERYTHING WORKING
            condition = True        #mark point as within obstacle i
        else:
            condition = False       #mark point as missing obstacle i
        inObstacles.append(condition)       #add collision condition to
    #print(inObstacles)
    return inObstacles

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
