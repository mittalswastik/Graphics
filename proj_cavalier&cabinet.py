from graphics import *
import numpy as np

WIDTH, HEIGHT = 500, 500

win1 = GraphWin('Cavalier Projection', WIDTH, HEIGHT)
win2 = GraphWin('Cabinet Projection', WIDTH, HEIGHT)
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
cavalier = np.array([[1,0,0.866],[0,1,0.5],[0,0,0]])
cabinet = np.array([[1,0,0.433],[0,1,0.25],[0,0,0]])
proj_cavalier = np.dot(cavalier,points)
proj_cabinet = np.dot(cabinet,points)
print(proj_cavalier)
proj_cavalier += 100
proj_cabinet += 100

p1 = Point(proj_cavalier[0][0],proj_cavalier[1][0])
p2 = Point(proj_cavalier[0][1],proj_cavalier[1][1])
p3 = Point(proj_cavalier[0][2],proj_cavalier[1][2])
p4 = Point(proj_cavalier[0][3],proj_cavalier[1][3])
p5 = Point(proj_cavalier[0][4],proj_cavalier[1][4])
p6 = Point(proj_cavalier[0][5],proj_cavalier[1][5])
p7 = Point(proj_cavalier[0][6],proj_cavalier[1][6])
p8 = Point(proj_cavalier[0][7],proj_cavalier[1][7])

points_cabinet = []
points_cabinet.append(Point(proj_cabinet[0][0],proj_cabinet[1][0]))
points_cabinet.append(Point(proj_cabinet[0][1],proj_cabinet[1][1]))
points_cabinet.append(Point(proj_cabinet[0][2],proj_cabinet[1][2]))
points_cabinet.append(Point(proj_cabinet[0][3],proj_cabinet[1][3]))
points_cabinet.append(Point(proj_cabinet[0][4],proj_cabinet[1][4]))
points_cabinet.append(Point(proj_cabinet[0][5],proj_cabinet[1][5]))
points_cabinet.append(Point(proj_cabinet[0][6],proj_cabinet[1][6]))
points_cabinet.append(Point(proj_cabinet[0][7],proj_cabinet[1][7]))

l1 =[]
l1.append(Line(p1,p2))
l1.append(Line(p2,p3))
l1.append(Line(p3,p4))
l1.append(Line(p4,p1))
l1.append(Line(p5,p6))
l1.append(Line(p6,p7))
l1.append(Line(p7,p8))
l1.append(Line(p8,p5))
l1.append(Line(p1,p5))
l1.append(Line(p2,p6))
l1.append(Line(p3,p7))
l1.append(Line(p4,p8))

l2 =[]
l2.append(Line(points_cabinet[1-1],points_cabinet[2-1]))
l2.append(Line(points_cabinet[2-1],points_cabinet[3-1]))
l2.append(Line(points_cabinet[3-1],points_cabinet[4-1]))
l2.append(Line(points_cabinet[4-1],points_cabinet[1-1]))
l2.append(Line(points_cabinet[5-1],points_cabinet[6-1]))
l2.append(Line(points_cabinet[6-1],points_cabinet[7-1]))
l2.append(Line(points_cabinet[7-1],points_cabinet[8-1]))
l2.append(Line(points_cabinet[8-1],points_cabinet[5-1]))
l2.append(Line(points_cabinet[1-1],points_cabinet[5-1]))
l2.append(Line(points_cabinet[2-1],points_cabinet[6-1]))
l2.append(Line(points_cabinet[3-1],points_cabinet[7-1]))
l2.append(Line(points_cabinet[4-1],points_cabinet[8-1]))

l = []
l.append(Line(a,b)) 
l.append(Line(b,c))
l.append(Line(c,d))
l.append(Line(d,a))
l.append(Line(p,q))
l.append(Line(q,r))
l.append(Line(r,s))   
l.append(Line(s,p))
l.append(Line(a,p))
l.append(Line(b,q))
l.append(Line(c,r))
l.append(Line(d,s))

for x in l1:
	x.draw(win1)
for x in l2:
	x.draw(win1)

win1.getMouse()
win1.close()

for x in l2:
	x.draw(win2)
for x in l:
	x.draw(win2)
win2.getMouse()
win2.close()
    # s = Rectangle(Point(300, 300), Point(350, 350))
    # s.draw(win)
    # s.setFill('blue')

    # while c.getCenter().getX() < WIDTH - RADIUS:
    #     c.move(10, 0)
    #     s.move(-10, 0)



