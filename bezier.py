from graphics import *
import numpy as np

degree = int(input("Please enter the degree of the bezier curve or type 1 for Custom->"))

win = GraphWin("Bezier Curve Final", 1000, 1000)

#initalization stuff
count = 0


if degree == 2 or degree == 1:
	M_vector = [[1,0,0],[-2,2,0],[1,-2,1]]
	count_till = 2
	if degree == 3:
		message = Text(Point(win.getWidth()/2, 20), 'Quadratic Bezier Curve')
	else:
		message = Text(Point(win.getWidth()/2, 20), 'Custom')
	message.draw(win)
elif degree == 3:
	M_vector = [[1,0,0,0],[-3,3,0,0],[3,-6,3,0],[-1,3,-3,1]]
	count_till = 3
	message = Text(Point(win.getWidth()/2, 20), 'Cubic Beizer Curve')
	message.draw(win)
else:
	print("Wrong Argument")
	exit()


# First point
if degree != 1:
	points = []
	point_on_screen = win.getMouse()
	points.append(point_on_screen)
	point_on_screen.draw(win)


	while count < count_till: 
		point_on_screen = win.getMouse()
		points.append(point_on_screen)
		point_on_screen.draw(win)

		controlpoint_line = Line(points[count], points[count+1])
		controlpoint_line.draw(win)
		count = count + 1


	x_vector = []
	y_vector = []
	plotList = []

	for p in points:
		x_vector.append([p.getX()])
		y_vector.append([p.getY()])

	t = np.linspace(0,1,num = 999,endpoint = False)



	for element in t:
		if degree == 2:
			t_vector = [[1,element,pow(element,2)]]
		elif degree == 3:
			t_vector = [[1,element,pow(element,2),pow(element,3)]]

		x = np.dot(t_vector,np.dot(M_vector, x_vector))
		y = np.dot(t_vector,np.dot(M_vector, y_vector))
		plotList.append(Point(x,y))

	for i in plotList:
		i.draw(win)

else: 

	for i in range(2):
		points =[]
		point_on_screen = win.getMouse()
		points.append(point_on_screen)
		point_on_screen.draw(win)

		while count < count_till: 
			point_on_screen = win.getMouse()
			points.append(point_on_screen)
			point_on_screen.draw(win)

		# controlpoint_line = Line(points[count], points[count+1])
		# controlpoint_line.draw(win)
			count= count + 1

		x_vector = []
		y_vector = []
		plotList = []

		for p in points:
			x_vector.append([p.getX()])
			y_vector.append([p.getY()])


		t = np.linspace(0,1,num = 999,endpoint = False)


		print(i)
		for element in t:
			t_vector = [[1,element,pow(element,2)]]
			x = np.dot(t_vector,np.dot(M_vector, x_vector))
			y = np.dot(t_vector,np.dot(M_vector, y_vector))
			plotList.append(Point(x,y))

		for i in plotList:
			i.draw(win)
		count = 0;
	# xCenter = points[1].getX()

	# reflectionpoints = []
	# x_vector = []
	# y_vector = []
	# plotList = []

	# for point in range(0,4):
	# 		newX = xCenter - points[point].getX()
	# 		mirror = Point(newX + xCenter, points[point].getY())
	# 		mirror.draw(win)
	# 		reflectionpoints.append(mirror)

	# # for point in range(0,3):
	# # 	linebtwreflectionpoints = Line(reflectionpoints[point], reflectionpoints[point+1])
	# # 	linebtwreflectionpoints.draw(win)

	# for p in reflectionpoints:
	# 	x_vector.append([p.getX()])
	# 	y_vector.append([p.getY()])

	# for element in t:
	# 	t_vector = [[1,element,pow(element,2),pow(element,3)]]
	# 	x = np.dot(t_vector,np.dot(M_vector, x_vector))
	# 	y = np.dot(t_vector,np.dot(M_vector, y_vector))
	# 	plotList.append(Point(x,y))

	# for i in plotList:
	# 	i.draw(win)

	# topLine = Line(points[0],reflectionpoints[0])
	# bottomLine = Line(points[3], reflectionpoints[3])
	# topLine.draw(win)
	# bottomLine.draw(win)

win.getMouse()

win.close()