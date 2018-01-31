import math
import turtle

def setUpWindow(screenObject):
	'''
	Changes range of x and y axis of window and changes the 	background color
	param list: (str) Variable assigned to the window
	return: (str) No return for this function
	'''
	screenObject.setworldcoordinates(-360, -1, 360, 1)
	screenObject.bgcolor("Blue")
	return

def setUpTurtle(turtleObject):
	'''
	Draws x and y axes and sets the turtle to the start position
	param list: (str) Variable assigned to the turtle
	return: (str) No return for this function
	'''
	turtleObject.up()
	turtleObject.goto(-360, 0)
	turtleObject.down()
	turtleObject.goto(360, 0)
	turtleObject.up()
	turtleObject.goto(0, -1)
	turtleObject.down()
	turtleObject.goto(0, 1)
	turtleObject.up()
	turtleObject.goto(-360, 0)
	turtleObject.down()
	return

def drawCosineCurve(turtleObject):
	'''
	Draws a cosine curve
	param list: (str) Variable assigned to the turtle
	return: (str) No return for this function
	'''
	turtleObject.up()
	turtleObject.goto(-360, 1)
	turtleObject.down()
	for i in range(-360, 360):
		y = math.cos(math.radians(i))
		print(y)
		turtleObject.goto(i, y)


def main():
	wn = turtle.Screen()
	mike = turtle.Turtle()
	screenObject = wn
	turtleObject = mike
	setUpWindow(screenObject)
	setUpTurtle(turtleObject)
	for i in range(-360, 360):
		y = math.sin(math.radians(i))
		print(y)
		mike.goto(i, y)
	drawCosineCurve(turtleObject)
	wn.exitonclick()
main()

