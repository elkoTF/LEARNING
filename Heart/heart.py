import turtle

start = turtle.Turtle()

turtle.bgcolor("Black")
start.pensize(2)

def curve():
    for i in range(200):
        start.right(1)
        start.forward(1)

start.color("red", "pink")
start.speed(0)
start.begin_fill()
start.left(140)
start.forward(111.65)
curve()
start.left(120)
curve()
start.forward(111.65)
start.penup()
start.goto(-60, 75)
start.write("I love you", font=("Arial", 20, "bold"))
start.hideturtle()
start.end_fill()
    
turtle.Screen().exitonclick()

