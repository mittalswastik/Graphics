from graphics import *
import math

win = GraphWin("Clipping", 300, 300)
center_x = int(input('Enter the center x of the circle: '))
center_y = int(input('Enter the center y of the circle: '))
radius = int(input('Enter the radius of the circle: '))
x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))


c = Circle(Point(center_x,center_y), radius)
c.setOutline('blue')
l1 = Line(Point(x1,y1),Point(x2,y2))
c.draw(win)
l1.draw(win)
win.getMouse()
win.close()



win1 = GraphWin("Clipping", 300, 300)
c1 = Circle(Point(center_x,center_y), radius)
m = (y2-y1)/(x2-x1)
a = 1 + (m**2)
b = (-(2*center_x) + (2*y1*m) - (2*center_y*m) - (2*(m**2)*x1))
c = ((center_x**2) + (y1**2) + (m**2)*(x1**2) + (center_y**2) - 2*center_y*y1 - 2*y1*m*x1 + 2*center_y*m*x1 - (radius**2))
delta = (b**2) - (4*a*c)

if delta <= 0:
	c.draw(win)
	c.draw(win)
	win.getMouse() # Pause to view result
	win.close()
else:
	sol_x1 = (-b-math.sqrt(delta))/(2*a)
	sol_x2 = (-b+math.sqrt(delta))/(2*a)
	sol_y1 = int(y1 + m*(sol_x1 - x1))
	sol_y2 = int(y1 + m*(sol_x2 - x1))

sol_x1 = int(sol_x1)
sol_x2 = int(sol_x2)

l2 = Line(Point(sol_x1,sol_y1),Point(sol_x2,sol_y2))
c1.draw(win1)
l2.draw(win1)
win1.getMouse() # Pause to view result
win1.close()
