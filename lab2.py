import turtle
import random
import os

def main():
	window = turtle.Screen()
	window.bgcolor('lightblue')

	michelangelo = turtle.Turtle()
	leonardo = turtle.Turtle()
	michelangelo.color('orange')
	leonardo.color('blue')
	michelangelo.shape('turtle')
	leonardo.shape('turtle')

	michelangelo.up()
	leonardo.up()
	michelangelo.goto(-100,20)
	leonardo.goto(-100,-20)

	x = random.randrange(0,301)
	y = random.randrange(0,301)
	leonardo.forward(x)
	michelangelo.forward(y)

	michelangelo.goto(-100,20)
	leonardo.goto(-100,-20)

	x = random.randrange(0,30)
	leonardo.forward(x)
	y = random.randrange(0,30)
	michelangelo.forward(y)
	x = random.randrange(0,30)
	leonardo.forward(x)
	y = random.randrange(0,30)
	michelangelo.forward(y)
	x = random.randrange(0,30)
	leonardo.forward(x)
	y = random.randrange(0,30)
	michelangelo.forward(y)
	x = random.randrange(0,30)
	leonardo.forward(x)
	y = random.randrange(0,30)
	michelangelo.forward(y)
	x = random.randrange(0,30)
	leonardo.forward(x)
	y = random.randrange(0,30)
	michelangelo.forward(y)
	x = random.randrange(0,30)
	leonardo.forward(x)
	y = random.randrange(0,30)
	michelangelo.forward(y)
	x = random.randrange(0,30)
	leonardo.forward(x)
	y = random.randrange(0,30)
	michelangelo.forward(y)
	x = random.randrange(0,30)
	leonardo.forward(x)
	y = random.randrange(0,30)
	michelangelo.forward(y)
	x = random.randrange(0,30)
	leonardo.forward(x)
	y = random.randrange(0,30)
	michelangelo.forward(y)
	x = random.randrange(0,30)
	leonardo.forward(x)
	y = random.randrange(0,30)
	michelangelo.forward(y)

	michelangelo.goto(-100,20)
	leonardo.goto(-100,-20)

	michelangelo.down()
	leonardo.down()

	michelangelo.forward(100)
	michelangelo.left(120)
	michelangelo.forward(100)
	michelangelo.left(120)
	michelangelo.forward(100)
	michelangelo.left(120)

	leonardo.forward(100)
	leonardo.right(90)
	leonardo.forward(100)
	leonardo.right(90)
	leonardo.forward(100)
	leonardo.right(90)
	leonardo.forward(100)
	leonardo.right(90)

	michelangelo.forward(300)
	michelangelo.left(72)
	michelangelo.forward(50)
	michelangelo.left(72)
	michelangelo.forward(50)
	michelangelo.left(72)
	michelangelo.forward(50)
	michelangelo.left(72)
	michelangelo.forward(50)
	michelangelo.left(72)
	michelangelo.forward(50)

	leonardo.forward(300)
	leonardo.right(60)
	leonardo.forward(50)
	leonardo.right(60)
	leonardo.forward(50)
	leonardo.right(60)
	leonardo.forward(50)
	leonardo.right(60)
	leonardo.forward(50)
	leonardo.right(60)
	leonardo.forward(50)
	leonardo.right(60)
	leonardo.forward(50)

	os.system("man man")
	os.system("man pwd")
	os.system("man mkdir")
	os.system("man rm")
	os.system("man cd")
	os.system("man ls")
	os.system("man mv")
	os.system("man cp")
	os.system("man python3")
	window.exitonclick()
main()