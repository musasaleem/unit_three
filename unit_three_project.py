# Name : Musa Saleem
# Date : 10 / 1
# Last Modified : 10 / 1
# Comments : On this project I made five crosses that connect with one another.
# I got the users input on what they wanted. Based on their desires of side length, and color.
# This turtle program draws a middle cross with four crosses attached to each of the primary positions:
# East, West, North and South.


import turtle
turtle.speed(12)


def side_length():
    """
    This function gets each consecutive side length that the user desires
    :return:
    """
    length = input("What is the length you want")
    return float(length)


def fill_color():
    """
    This function gets the inside color of the cross that the user desires
    :return:
    """
    color = input("what do you want the inside color of the cross to be?")
    return color


def cross(length, color):
    """
    Is the process for drawing a single cross
    :param length:
    :param color:
    :return:
    """
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
    """
    Moves turtle to new location without drawing a line
    :param x:
    :param y:
    :return:
    """
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
