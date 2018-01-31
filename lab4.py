'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(turtle, width, top_left_x, top_left_y) - to outline dartboard
  drawLine(turtle, x_start, y_start, x_end, y_end) - to draw axes
  drawCircle(turtle, radius) - to draw the circle
  setUpDartboard(screen, turtle) - to set up the board using the above functions
  inCircle(turtle, circle_center, radius) - determine if dot is in circle
  throwDart(turtle)
  montePi(turtle, num_darts) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

# List constants here (NO MAGIC NUMBERS!):
BATCH_OF_DARTS = 5000
BOARD_WIDTH = 2
RIGHT_ANGLE = 90

def setUpDartboard(window, darty):
	window.setworldcoordinates(-1, -1, 1, 1)
	darty.up()
	darty.goto(0, -1)
	darty.down()
	darty.circle(1, steps=360)
	darty.up()
	darty.goto(-1, 0)
	darty.down()
	darty.goto(1, 0)
	darty.up()
	darty.goto(0, -1)
	darty.down()
	darty.goto(0, 1)
	
def throwDart(darty):
	xval = random.uniform(-1, 1)
	yval = random.uniform(-1, 1)
	darty.up()
	darty.goto(xval, yval)
	darty.stamp()

def montePi(number_darts, darty):
	circle_darts = 0
	darty.up()
	for i in range(number_darts):
		xval = random.uniform(-1, 1)
		yval = random.uniform(-1, 1)
		darty.goto(xval, yval)
		if (darty.distance(0,0) < 1):
			darty.color("blue")
			darty.stamp()
			circle_darts += 1
		else:
			darty.color("red")
			darty.stamp()
	return(4*(circle_darts/number_darts))

def game(darty):
	darty.up()
	player_one = 0
	player_two = 0
	for i in range(10):
		darty.color("green")
		throwDart(darty)
		if (darty.distance(0, 0) < 1):
			player_one +=1
		darty.color("orange")
		throwDart(darty)
		if (darty.distance(0, 0) < 1):
			player_two +=1
	if (player_one > player_two):
		print("Player One Wins!")
	elif (player_one < player_two):
		print("Player Two Wins!")
	elif (player_one == player_two):
		print("It's a tie!")
		

def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)

    print("\tPart A Complete...")
    print("=========== Part B ===========")
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(number_darts, darty)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    # Don't hide or mess with window while it's 'working'
    game(darty)
    window.exitonclick()

main()
