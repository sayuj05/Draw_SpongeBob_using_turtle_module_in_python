import turtle
turtle.Screen()
turtle.bgcolor("#F4C2C2")
sayuj = turtle.Turtle()
sayuj.pensize(5)

# body​
sayuj.penup()
sayuj.goto(-70, -70)
sayuj.pendown()
sayuj.fillcolor("yellow")
sayuj.begin_fill()
sayuj.forward(200)
sayuj.left(90)
sayuj.forward(200)
sayuj.left(90)
sayuj.forward(200)
sayuj.left(90)
sayuj.forward(200)

sayuj.end_fill()


# brownpants​
sayuj.fillcolor("brown")
sayuj.begin_fill()
sayuj.forward(40)
sayuj.left(90)
sayuj.forward(200)
sayuj.left(90)
sayuj.forward(40)
sayuj.left(90)
sayuj.forward(200)
sayuj.left(90)
sayuj.end_fill()


# shirts​
sayuj.fillcolor("white")
sayuj.begin_fill()
sayuj.forward(20)
sayuj.left(90)
sayuj.forward(200)
sayuj.left(90)
sayuj.forward(20)
sayuj.left(90)
sayuj.forward(200)
sayuj.end_fill()

sayuj.penup()


# tie​
sayuj.left(90)

sayuj.forward(18)
sayuj.left(90)
sayuj.forward(100)
sayuj.fillcolor("red")
sayuj.begin_fill()
sayuj.pencolor("red")
sayuj.pendown()
sayuj.circle(7)
sayuj.end_fill()


sayuj.penup()

# eye​
sayuj.pencolor("black")
sayuj.goto(75, 50)
sayuj.pendown()
sayuj.fillcolor("white")
sayuj.begin_fill()
sayuj.circle(25)
sayuj.end_fill()

sayuj.fillcolor("black")
sayuj.penup()
sayuj.goto(80, 60)
sayuj.begin_fill()
sayuj.circle(10)
sayuj.end_fill()

# eye2​
sayuj.penup()
sayuj.pencolor("black")
sayuj.goto(-15, 50)
sayuj.pendown()
sayuj.fillcolor("white")
sayuj.begin_fill()
sayuj.circle(25)
sayuj.end_fill()

sayuj.penup()
sayuj.goto(-10, 60)
sayuj.fillcolor("black")
sayuj.begin_fill()
sayuj.circle(10)
sayuj.end_fill()


# smile​
sayuj.penup()
sayuj.goto(-10, 0)
sayuj.pendown()
sayuj.pensize(5)
sayuj.right(90)
sayuj.fillcolor("red")
sayuj.begin_fill()
sayuj.circle(40, 180)
sayuj.left(90)
sayuj.forward(80)
sayuj.end_fill()


# teeths​
sayuj.fillcolor("white")
sayuj.begin_fill()
sayuj.left(180)
sayuj.forward(25)
sayuj.right(90)
sayuj.forward(15)
sayuj.left(90)
sayuj.forward(10)
sayuj.left(90)
sayuj.forward(15)
sayuj.end_fill()


sayuj.fillcolor("white")
sayuj.begin_fill()
sayuj.right(90)
sayuj.forward(10)
sayuj.right(90)
sayuj.forward(15)
sayuj.left(90)
sayuj.forward(10)
sayuj.left(90)
sayuj.forward(15)
sayuj.end_fill()


def main():
    print('Painting the Cartoon... ')
    style = ('Lucida Handwriting', 20, 'bold')
    sayuj.penup()
    sayuj.pensize(5)
    sayuj.goto(-180, -180)
    sayuj.write("SpongeBob by Sayuj ", font=style, align='left')
    turtle.hideturtle()
    turtle.mainloop()


if __name__ == '__main__':
    main()
