import turtle
screen = turtle.Screen()

turtle.speed(0)
turtle.goto(100, 0)
turtle.goto(100, 100)
turtle.goto(0, 100)
turtle.goto(0, 0)

turtle.up()
turtle.goto(50, 50 - 15)
turtle.down()
turtle.circle(15)

screen.exitonclick()
