import turtle
 
# def f(length, depth):
#    if depth == 0:
#      forward(length)
#    else:
#      f(length/3, depth-1)
#      right(60)
#      f(length/3, depth-1)
#      left(120)
#      f(length/3, depth-1)
#      right(60)
#      f(length/3, depth-1)
 
# f(500, 4)

def koch(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """

    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3)   # Go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)

T = turtle.Turtle()
win = turtle.Screen()
T.left(180)
T.penup()
T.forward(500)
T.left(180)
T.pendown()

T.pencolor("red")
koch(T,4,500)

T.pencolor("blue")
T.left(-120)
koch(T,4,500)

T.pencolor("green")
T.left(-120)
koch(T,4,500)
win.exitonclick()