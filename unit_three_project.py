import turtle
turtle.speed(12)


def side_length():
    length = input("What is the length you want")
    return float(length)


def cross(length):
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


def move(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def main():
    length = side_length()
    cross(length)
    move(120, 0)
    turtle.left(90)
    cross(length)
    move(240, 0)
    turtle.left(90)
    cross(length)
    move(160,-40)
    cross(length)
    move(200,80)
    turtle.right(90)
    cross(length)

    turtle.exitonclick()


main()
