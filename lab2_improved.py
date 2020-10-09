import math
import random
import turtle

needlesNum = int(input("How many needles do you want? "))

def buffonNeedle(numNeedles):
    jeff = turtle.Turtle()
    turtle.tracer(0,0)
    screen = turtle.Screen()
    unit = 100

    #creates the two lines
    jeff.up()
    jeff.goto((-2 * unit), (1/2 * unit))
    jeff.down()
    jeff.goto((2 * unit), (1/2 * unit))

    jeff.up()
    jeff.goto((-2 * unit), (-1/2 * unit))
    jeff.down()
    jeff.goto((2 * unit), (-1/2 * unit))
    jeff.up()

    needlesInCounter = 0

    #executes for every needle
    for i in range(numNeedles):
        x = random.uniform(-2 * unit, 2 * unit)
        y = random.uniform(-unit, unit)
        angle = (random.uniform(0.0, math.pi))

        #checks which line the needle is closer to
        if y > 0:
            distance = (abs(((1/2 * unit) - y) / unit))
        else:
            distance = (abs(((-1/2 * unit) - y) / unit))

        #checks if the needle is touching the line
        if distance <= (1/2 * math.sin(angle)):
            needlesInCounter += 1
            jeff.pencolor('green')
        else:
            jeff.pencolor('red')

        jeff.goto(x, y)
        jeff.down()
        jeff.setheading(math.degrees(angle))
        jeff.forward(1/2 * unit)
        jeff.backward(unit)
        jeff.up()

    jeff.hideturtle()
    turtle.update()
    screen.exitonclick()

    estimPi = (2 * numNeedles) / (needlesInCounter)
    return estimPi

print(buffonNeedle(needlesNum))
