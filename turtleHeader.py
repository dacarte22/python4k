import turtle

t = turtle.Pen()
screen = turtle.Screen()


def mycircle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()


def mysquareFrame(size):
    for x in range(1, 5):
        t.forward(size)
        t.left(90)

def mysquareFill(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()

def mystar(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    if filled == True:
        t.end_fill()


def squareOutlines():
    mysquareFrame(25)
    mysquareFrame(50)
    mysquareFrame(75)
    mysquareFrame(100)
    mysquareFrame(125)

def fillSquare(t):
    t.begin_fill()
    mysquareFrame(50)
    t.end_fill()



def yellowStarNoOutline(t):
    t.color(0.9, 0.75, 0)
    mystar(120, True)

def main():
    #t = turtle.Pen()
    #screen = turtle.Screen()

    
    yellowStarNoOutline(t)



    screen.exitonclick()
