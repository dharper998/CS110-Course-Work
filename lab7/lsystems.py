import turtle
import random

def applyRules(char, rules):
	'''
	Applies each rule to a character from the axiom
	paramlist: char (the current character in the axiom being tested against rules), rules (the list of instructions for transforming characters)
	return: newchar (the result after appling rules)
	'''
	newchar = ''
	for i in range(len(rules)):
		rule = rules[i]
		splitrule = rule.split(":")
		if char == splitrule[0]:
			newchar = splitrule[1]
			break
		else:
			newchar = char
	return newchar

def processString(axiom, rules):
	'''
	Loops through each character in the axiom and applies the rules to it
	paramlist: axiom (the starting string given by the user), rules (the list of instructions for transforming characters)
	return: newstr (the new string created after applying the rules to each character in the axiom)
	'''
	newstr = ""
	for i in range(len(axiom)):
		newstr += applyRules(axiom[i], rules)
	return newstr

def createLSystem(iterations, axiom, rules):
	'''
	Creates an L System by transforming the characters in the axiom a given number of times based on given rules
	paramlist: iterations (the number of times the axiom should be altered), axiom (the starting string given by the user), rules (the list of instructions for transforming characters)
	return: newstr (the final string created after running through the given number of iterations)
	'''
	newstr = axiom
	for i in range(iterations):
		newstr = processString(newstr, rules)
	return newstr


def drawLSystem(orders, distance, degree):
	'''
	Moves the turtle based on the L System created
	paramlist: orders (the L System created after applying rules for the given number of iterations), distance (the forward distance the turtle moves), degree (the angle at which the turtle turns)
	return: none
	'''
	mike = turtle.Turtle()
	wn = turtle.Screen()
	for i in range(len(orders)):
		mike.color(random.choice(['red', 'green', 'blue', 'black']))
		mike.width(random.randrange(1, 4))
		if orders[i] == "F":
			mike.forward(distance)
		elif orders[i] == "+":
			mike.right(degree)
		elif orders[i] == "-":
			mike.left(degree)
	wn.exitonclick()
