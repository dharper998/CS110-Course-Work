import turtle

def seq3np1(n):
	'''
	Performs the 3n+1 operation and tracks the number of iterations required to reach 1
	paramlist: n (the inputted value to be converted)
	return: count (the result of the 3n+1 equation)
	'''
	count = 0
	while (n != 1):
		if n % 2 == 0:
			n = n / 2
		else:
			n = 3*n + 1
		count += 1
	return count

def writeTurtle(i, max_so_far, dave):
	'''
	Writes out the current greatest value for the number of iterations
	paramlist: i (the current value in the range of the for loop), max_so_far (the current greatest value for the number of iterations), dave (the turtle that writes out the current maximum)
	return: none
	'''
	dave.clear()
	dave.up()
	dave.goto(0, max_so_far)
	dave.write("Maximum so far: " + str(i) + ", " + str(max_so_far))

def graph(start, i, numit, max_so_far, mike):
	'''
	Draws the graph of iterations required for each value in the given range
	paramlist: start (the range from 1 up to and including the inputted upper bound), i (the current value in the range of the for loop), numit (the number of iterations required for i), max_so_far (the current highest number of iterations), mike (the turtle that draws the graph)
	return: none
	'''
	turtle.setworldcoordinates(0, 0, i+10, max_so_far+10)
	result = numit
	mike.goto(i, result)

def main():
	n = int(input("Enter a number: "))
	print(seq3np1(n))
	upbound = int(input("What would you like the upper bound to be?: "))
	start = range(1, upbound+1)
	wn = turtle.Screen()
	mike = turtle.Turtle()
	dave = turtle.Turtle()
	turtle.setworldcoordinates(0, 0, 10, 10)
	max_so_far = 0
	for i in (start):
		numit = seq3np1(i)
		if numit > max_so_far:
			max_so_far = numit
			writeTurtle(i, max_so_far, dave)
		print("The number of iterations required for " + str(i) + " is " + str(numit))
		graph(start, i, numit, max_so_far, mike)
	wn.exitonclick()
main()
