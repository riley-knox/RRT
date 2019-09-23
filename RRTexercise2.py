#import python3 print function
from __future__ import print_function

#import required modules
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math
import pprint

#program parameters
k = 50              #number of iterations
d = 1               #defined step length; not used as variable as all steps are unit vectors (have inherent length = 1)
pointsList = []     #blank list to hold point data; has form ['point name', point coordinates, 'parent point']
segmentsList = []   #blank list to hold line segment endpoint coordinates
obstaclesList = []  #blank list to hold obstacle coordinates and radii

#fix random seed
np.random.seed(34725534)

#define distance calculation function
def calcDist(x1,x2,y1,y2):
    dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return dist

#define function to check if a point IS inside an obstacle
def isinObstacle(x,y):
    distList = []      #empty list to hold distances to each obstacle center
    for i in range(len(obstaclesList)):
        obDist = calcDist(x,obstaclesList[i][0][0],y,obstaclesList[i][0][1]) #calculate distance to each obstacle center
        #print('distance to obstacle {}: '.format(i+1), obDist)
        distList.append(obDist)
        if obDist <= obstaclesList[i][1]:
            print('Point within obstacle {}!'.format(i+1))
        else:
            pass


#create start point
startX = 20         #x coordinate
startY = 20         #y coordinate
startColor = '#1ca120'
startName = 'q0'    #name
startData = [startName,(startX,startY)] #pointsList data entry
pointsList.append(startData)
#create end point
endX = 75
endY = 75
endColor = '#ff9b00'

#generate obstacles
#number of obstacles
N = 10
#x- and y-coordinates of obstacles on 0-100 scale
x = 100*np.random.rand(N)
y = 100*np.random.rand(N)
centers = [(x,y) for x,y in zip(x,y)]
#obstacle sizes
radii = (10*np.random.rand(N))
#make list of obstacle properties
for i in range(N):
   obstacleCenter = centers[i]
   obstacleRadius = radii[i]
   obstacleProps = (obstacleCenter,obstacleRadius)
   obstaclesList.append(obstacleProps)
pprint.pprint(obstaclesList) #print list of obstacle coordinates & radii - CAN DELETE IF EVERYTHING IS WORKING

#make sure start and end points are not inside an obstacle
isinObstacle(startX,startY)

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
