import turtle
'''
#creating canvas
turtle.Screen().bgcolor("white")
sc=turtle.Screen()
sc.setup(600,300)
board=turtle.Turtle()
board.speed(1)
board.color("orange","orange") #outline color, fill color
board.begin_fill()

for i in range(4):
    board.forward(100)
    board.left(90)
board.end_fill()
turtle.done()
'''

'''
turtle.Screen().bgcolor("White")
board=turtle.Turtle()
board.speed(2)
board.color("orange","black")

#start filling
board.begin_fill()

#first triangle
board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

#second triangle
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

board.end_fill()

turtle.done()
'''
t=turtle.Turtle()
s=turtle.Screen()
colors=['red','purple','blue','green','orange','yellow']
s.bgcolor('black')
t.speed(10)
t.hideturtle()
while True:
    for x in range(200):
        t.pencolor(colors[x%len(colors)])
        t.width(x/100+1)
        t.forward(x)
        t.left(59)
    t.right(239)
    for x in range(200,0,-1):
        t.pencolor('black')
        t.width(x/100+7)
        t.forward(x)
        t.right(59)