##a = input()
##b = input()

##result = a*b
##result1 = a/b
##result2 = a+b
##result3 = a-b

##print(a, "/", b, "=", result1)
##print(a, "*", b, "=", result)
##print(a, "+", b, "=", result2)
##print(a, "-", b, "=", result3)

##data = "안녕 \n 하세요 \n 파이썬!"
##print(data) 

##import turtle

##turtle.shape('turtle')

##t = turtle.Turtle()

##turtle.shape ("arrow")

##t.speed(3)
##t.pensize(10)
##t.pencolor("red")


##t.forward(200)
##t.right(144)
##t.forward(200)
##t.right(144)
##t.forward(200)
##t.right(144)
##t.forward(200)
##t.right(144)
##t.forward(200)


##turtle.done()


import turtle
import random
def screenLeftClick(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)

def screenRightClick(x, y):
    global r, g, b

    r = random.random()
    g = random.random()
    b = random.random()

    turtle.pencolor((r, g, b))
    turtle.penup()
    turtle.goto(x, y)
        
def screenMidClick(x, y):
            global r, g, b
            tSize = random.randrange(1, 10)
            turtle.pensize(tSize)

            r = random.random()
            g = random.random()
            b = random.random()

            pSize = 10
            r, g, b = 0.0, 0.0, 0.0

pSize = 10
r = 0.0
g = 0.0
b = 0.0

turtle.title("거북이로 그림 그리기")
turtle.shape("turtle")
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick, 3)
turtle.onscreenclick(screenMidClick, 2)

turtle.done()