
from turtle import Turtle, Screen, mainloop

tim = Turtle()
screen = Screen()


def move_foward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():

    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_foward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
mainloop()
