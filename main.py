from turtle import Turtle, Screen

bill = Turtle()
screen = Screen()


# direction functions
def move_forwards():
    bill.forward(10)


def move_backwards():
    bill.backward(10)


def move_clockwise():
    bill.right(10)


def move_counter_clockwise():
    bill.left(10)


def clear():
    bill.clear()
    bill.reset()


# event listener
screen.listen()

# controls
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
