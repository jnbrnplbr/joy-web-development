import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)

# Draw a heart shape
t.begin_fill()
t.fillcolor("red")
t.left(140)
t.forward(224)
t.circle(-112, 200)
t.left(120)
t.circle(-112, 200)
t.forward(224)
t.end_fill()

# Move to write text
t.penup()
t.goto(-70, 0)
t.pendown()
t.color("white")
t.write("I love you, Brian", font=("Arial", 16, "bold"))

# Finish
t.hideturtle()
turtle.done()
