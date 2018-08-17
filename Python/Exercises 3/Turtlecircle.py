import turtle, random
turtle.bgcolor("black")
benny = turtle.Turtle()
colors = ["red","green","blue","orange","purple","pink","yellow","purple","blue"] #List of colors

benny.width(1)
benny.hideturtle()
for i in range(250):
    color = random.choice(colors)
    benny.circle(25+i*2.5)
    benny.forward(-i)
    benny.left(10)
    benny.width(1+i/10)
    benny.color(color)
