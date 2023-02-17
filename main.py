# Flappy Bird
import turtle
import random
from threading import*
import math
import multiprocessing as mp
wn = turtle.Screen()
t = turtle.Turtle()
p = turtle.Turtle()

wn.screensize(600, 500)
wn.bgpic('background.gif')
Bird = 'Bird.gif'
wn.addshape(Bird)
t.shape(Bird)
t.penup()
x = -150
y = 0
t.goto(x, y)
wn.listen()

#PIPES
pipe = 'PIPE.gif'
wn.addshape(pipe)
p.shape(pipe)
p.hideturtle()
p.penup()
p.speed(0)
p.goto(300, 0)

def collision():
    global score
    dx = t.xcor() - p.xcor()
    dy = t.ycor() - p.ycor()
    distance = math.sqrt(dx ** 2 + dy ** 2)
    check = False
    if distance < 20 and not check:
        exit()

def movingp():  # movingp is variable for moving pipes and generates new ones randomly
    while (1 == 1):
        list = [-150, -100, -50, 0, 50, 100, 150, 200, 250]
        i = 0
        p.goto(300, 0)
        while (i < 60):
            p.showturtle()
            p.backward(10)
            i = i + 1
            if (i == 60):
                i = 0
                p.hideturtle()
                p.goto(-300, -1000)
                p.goto(300, -1000)
                p.goto(300, random.choice(list))

def jump():
    y = t.ycor() + 25
    t.goto(-150, y)

    while 3 == 3:
        t.speed(1)
        t.goto(-150, -200)
        t.goto(-150, t.ycor())


# DETECT USER INPUTS
wn.onkeypress(jump, 'space')

# TWO THREADS FOR TWO CODES TO RUN SIMULTANEOUSLY
def movingpipes():

    while 2 == 2:
        movingp()
        pass

pipethread = Thread(target=movingpipes, daemon=True)
pipethread.start()

wn.mainloop()
wn.exitonclick()







wn.mainloop()
wn.exitonclick()
