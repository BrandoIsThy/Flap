import turtle
import random
import time


r = random
wn = turtle.Screen()
wn.screensize(600, 500)

wn.bgpic('background.gif')
PU1 = turtle.Turtle()
PD1 = turtle.Turtle()
PU2 = turtle.Turtle()
PD2 = turtle.Turtle()
PU3 = turtle.Turtle()
PD3 = turtle.Turtle()
PU4 = turtle.Turtle()
PD4 = turtle.Turtle()
PU5 = turtle.Turtle()
PD5 = turtle.Turtle()


v1u = 'pipes/v1u.gif'
wn.addshape(v1u)
PU1.shape(v1u)
PU1.hideturtle()
PU1.penup()
PU1.speed(0)
PU1.goto(300, 233)


v1d = 'pipes/v1d.gif'
wn.addshape(v1d)
PD1.hideturtle()
PD1.shape(v1d)
PD1.penup()
PD1.speed(0)

PD1.goto(300, -60)

v2d = 'pipes/v2d.gif'
wn.addshape(v2d)
PD2.shape(v2d)
PU2.hideturtle()
PD2.penup()
PD2.speed(0)
PD2.goto(300, -143)

v2u = 'pipes/v2u.gif'
wn.addshape(v2u)
PU2.shape(v2u)
PD2.hideturtle()
PU2.penup()
PU2.speed(0)
PU2.goto(300, 160)

v3u = 'pipes/Var3.UP.gif'
wn.addshape(v3u)
PU3.shape(v3u)
PU3.hideturtle()
PU3.penup()
PU3.speed(0)
PU3.goto(300, 104)

v3d = 'pipes/Var3.DOWN.gif'
wn.addshape(v3d)
PD3.shape(v3d)
PD3.hideturtle()
PD3.penup()
PD3.speed(0)
PD3.goto(300,-185)

v4u = 'pipes/VAR4.UP.gif'
wn.addshape(v4u)
PU4.shape(v4u)
PU4.hideturtle()
PU4.penup()
PU4.speed(0)
PU4.goto(300, 194)

v4d = 'pipes/VAR4,DOWN.gif'
wn.addshape(v4d)
PD4.shape(v4d)
PD4.hideturtle()
PD4.penup()
PD4.speed(0)
PD4.goto(300, -97)

v5u = 'pipes/VAR5.UP.gif'
wn.addshape(v5u)
PU5.shape(v5u)
PU5.hideturtle()
PU5.penup()
PU5.speed(0)
PU5.goto(300, 60)

v5d = 'pipes/VAR5.DOWN.gif'
wn.addshape(v5d)
PD5.shape(v5d)
PD5.hideturtle()
PD5.penup()
PD5.speed(0)
PD5.goto(300, -230)

def start():
    while(1==1):
        list = [1, 2, 3, 4, 5]
        ratio = 1
        if random.choice(list) == 1:
            PU1.showturtle()
            PD1.showturtle()
            PU1.speed((10) * ratio)
            PD1.speed((10) * ratio)
            if PU1.xcor() > -300:
                for location in range(40):
                    PU1.backward(15)
                    PD1.backward(15)
            if PU1.xcor() == -300:
                PU1.hideturtle()
                PD1.hideturtle()
                PU1.speed(0)
                PD1.speed(0)
                PU1.goto(300, 233)
                PD1.goto(300, -60)
        elif random.choice(list) == 2:
            PU2.showturtle()
            PD2.showturtle()
            PD2.speed((10) * ratio)
            PU2.speed((10) * ratio)
            if PU2.xcor() > -300:
                for location in range(40):
                    PU2.backward(15)
                    PD2.backward(15)

            if PU2.xcor() == -300:
                PU2.hideturtle()
                PD2.hideturtle()
                PU2.speed(0)
                PD2.speed(0)
                PU2.goto(300, 160)
                PD2.goto(300, -143)


        elif random.choice(list) == 3:
            PU3.showturtle()
            PD3.showturtle()
            PD3.speed((10) * ratio)
            PU3.speed((10) * ratio)

            if PU3.xcor() > -300:
                for location in range(40):
                    PU3.backward(15)
                    PD3.backward(15)
            if PU3.xcor() == -300:
                PU3.hideturtle()
                PD3.hideturtle()
                PU3.speed(0)
                PD3.speed(0)
                PU3.goto(300, 104)
                PD3.goto(300, -185)

        elif random.choice(list) == 4:
            PU4.showturtle()
            PD4.showturtle()
            PD4.speed((10) * ratio)
            PU4.speed((10) * ratio)

            if PU4.xcor() > -300:
                for location in range(40):
                    PU4.backward(15)
                    PD4.backward(15)
            if PU4.xcor() == -300:
                PU4.hideturtle()
                PD4.hideturtle()
                PU4.speed(0)
                PD4.speed(0)
                PU4.goto(300, 194)
                PD4.goto(300, -97)

        else:
            PU5.showturtle()
            PD5.showturtle()
            PD5.speed((10) * ratio)
            PU5.speed((10) * ratio)

            if PU5.xcor() > -300:
                for location in range(40):
                    PU5.backward(15)
                    PD5.backward(15)
            if PU5.xcor() == -300:
                PU5.hideturtle()
                PD5.hideturtle()
                PU5.speed(0)
                PD5.speed(0)
                PU5.goto(300, 60)
                PD5.goto(300, -230)




wn.listen()
wn.onkeypress(start, 'y')


#IF THERE IS NO IMPACT, X=1, IF THERE IS WE MAKE IT THAT IMPACT CAUSES X = 2


#List of turtles FIND A WAY TO LOOP THIS BUT THIS WORKS






wn.mainloop()

#Create List, find out how to do ordered pair????
#In given list, Cause them to Appear at a point just beyond the screen, x= 300 is fine
#Create a When statement for when the lower pipe hits 0 to create a New set of pipes?