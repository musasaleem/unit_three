# Name : Musa Saleem
# Date : 9 / 28
# Last Modified : 9 / 28
# Comments : On this project I made five crosses that connect with one another



import turtle
turtle.speed(12)


def side_length():
    length = input("What is the length you want")
    return float(length)


def fill_color():
    """
    This function gets the inside color of the cross
    :return:
    """
    color = input("what do you want the inside color of the cross to be?")
    return color


def cross(length, color):
    turtle.color(color)
    turtle.begin_fill()

    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.end_fill()

def move(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def main():
    length = side_length()
    color = fill_color()
    cross(length, color)
    move(3 * length, 0)
    turtle.left(90)
    cross(length, color)
    move(6 * length, 0)
    turtle.left(90)
    cross(length, color)
    move(4 * length, -length)
    cross(length, color)
    move(5 * length, 2 * length)
    turtle.right(90)
    cross(length, color)

    turtle.exitonclick()


main()
