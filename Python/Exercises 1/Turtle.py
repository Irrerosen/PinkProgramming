import turtle

#You cam give your turtle any name you want
betty = turtle.Turtle()
from turtle import*
betty.color('red', 'yellow')
betty.begin_fill()
#SQUARE
# for i in range(4):
#     betty.forward(90)  #amount of steps
#     betty.right(90)     #degrees angle turn
#HEXAGON
# for i in range(6):
#     betty.forward(30)  #amount of steps
#     betty.right(60)     #degrees angle turn
#   betty.forward(100)
#   betty.right(120)
#FLOWER
betty.left(180)
for i in range (36):
      betty.forward(250)
      betty.left(170)
betty.end_fill()
# #ROBOT
# def drawarm(colorin):
#     color = colorin
#     betty.color(color, color)
#     betty.begin_fill()
#     for i in range(2):
#         betty.left(90)
#         betty.forward(20)
#         betty.left(90)
#         betty.forward(100)
#         print(betty.pos())
#     betty.end_fill()
# def drawleg(colorin):
#     color = colorin
#     betty.color(color, color)
#     betty.begin_fill()
#     for i in range(2):
#         betty.left(90)
#         betty.forward(20)
#         betty.left(90)
#         betty.forward(50)
#     betty.end_fill()
# def draweye(insidecol,outsidecol):
#     color1 = insidecol
#     color2 = outsidecol
#     betty.color(color2,color1)
#     betty.begin_fill()
#     betty.pensize(4)
#     betty.circle(10)
#     betty.end_fill()
# def moveme(coordx,coordy):
#     betty.penup()
#     betty.setx(coordx)
#     betty.sety(coordy)
#     betty.pendown()
# betty.color("blue", "blue")
# betty.begin_fill()
# for i in range (2):
#     betty.forward(100)
#     betty.right(90)
#     betty.forward(150)
#     betty.right(90)
# betty.end_fill()
# betty.left(90)
# moveme(0,0)
# drawarm("orange")
# moveme(120,0)
# drawarm("orange")
# moveme(100,-150)
# drawleg("orange")
# moveme(20,-150)
# drawleg("orange")
# moveme(0,0)
# betty.right(90)
# betty.color("green", "green")
# betty.begin_fill()
# betty.forward(100)
# betty.left(100)
# betty.forward(60)
# betty.left(80)
# betty.forward(80)
# betty.left(80)
# betty.forward(60)
# betty.end_fill()
# betty.left(100)
# moveme(30,20)
# draweye("black","white")
# moveme(70,20)
# draweye("black","white")
# moveme(20,10)
# betty.pensize(3)
# betty.color("red")
# betty.begin_fill()
# betty.forward(60)
# betty.end_fill()
# betty.hideturtle()
turtle.done()
