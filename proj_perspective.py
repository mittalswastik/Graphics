from graphics import *
import numpy as np

WIDTH, HEIGHT = 500, 500

win1 = GraphWin('Perspective Projection', WIDTH, HEIGHT)


a = Point(0,0)
b = Point(100,0)
c = Point(100,100)
d = Point(0,100)
p = Point(0,0)
q = Point(100,0)
r = Point(100,100)
s = Point(0,100)
# points = np.array([[320,150,0,1],[220,150,0,1],[150,200,0,1],[250,200,0,1],[320,300,0,1],[220,300,0,1],[150,400,0,1],[250,400,0,1]])
points = np.array([[0,100,100,0,0,100,100,0],[0,0,100,100,0,0,100,100],[0,0,0,0,100,100,100,100]])
a1 = 2e-3
a2 = 3e-4
a3 = 2e-16
div = a1*points[0] + a2*points[1] + a3*points[2] + 1

points = points/(div)
print(points)

points += 100
points_perspective = []
for i in range(8):
	points_perspective.append(Point(points[0][i],points[1][i]))

l =[]
l.append(Line(points_perspective[0],points_perspective[1]))
l.append(Line(points_perspective[1],points_perspective[2]))
l.append(Line(points_perspective[2],points_perspective[3]))
l.append(Line(points_perspective[3],points_perspective[0]))
l.append(Line(points_perspective[4],points_perspective[5]))
l.append(Line(points_perspective[5],points_perspective[6]))
l.append(Line(points_perspective[6],points_perspective[7]))
l.append(Line(points_perspective[7],points_perspective[4]))
l.append(Line(points_perspective[0],points_perspective[4]))
l.append(Line(points_perspective[1],points_perspective[5]))
l.append(Line(points_perspective[2],points_perspective[6]))
l.append(Line(points_perspective[3],points_perspective[7]))


for x in l:
	x.draw(win1)
win1.getMouse()
win1.close()
