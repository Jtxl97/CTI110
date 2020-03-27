#Assign a value for forward motion to a variable
#Using a while statement, add value to the varible until the variable
#has reached a value that equals it's original value multipled by 100
#500 in this case, 5 being the original value
#Use your variable as the value for every forward motion
#After every forward motion turn right 90 degrees

import turtle
turtle.shape("turtle")
turtle.setup(1000,1000)

#This is to start design off center as to avoid it drawing off screen
turtle.penup()
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)

turtle.pendown()

f = 5
while f < 500:
    f += 5

    turtle.forward(f)
    turtle.right(90)
    turtle.forward(f)
    turtle.right(90)
    turtle.forward(f)
    turtle.right(90)
    turtle.forward(f)
    turtle.right(90)

turtle.hideturtle()
