import turtle

class LSystem:
	def __init__(self, filename):
		loop = True
		while loop == True:
			try:
				self.inputfile = open(filename, "r")
				loop = True
				break
			except:
				filename = input("Invalid File Name, Enter a Valid File Name: ")

		self.angle = int(self.inputfile.readline())
		self.iterations = int(self.inputfile.readline())
		self.axiom = self.inputfile.readline().strip()
		self.rules = {}
		for line in self.inputfile:
			line = line.strip()
			splitrule = line.split(":")
			index = splitrule[0].strip()
			if len(splitrule) == 2:
				rule = splitrule[1].strip()
			else:
				rule = ""
			self.rules[index] = rule
		self.orders = self.createLSystem()

	def createLSystem(self):
		'''
		Runs the rules on the axiom a given number of times
		Paramlist: none
		Return: createstr (The final string created after running all iterations of rule application)
		'''
		createstr = self.axiom
		for i in range(self.iterations):
			createstr = self.processString(createstr)
		return createstr

	def processString(self, createstr):
		'''
		Creates a new string by looping through the characters in the current iteration of the string and applying the rules
		Paramlist: createstr (The current iteration of the string)
		Return: processstr (The new string created after applying the rules to the current string)
		'''
		processstr = ""
		for i in range(len(createstr)):
			processstr += self.applyRules(createstr[i])
		return processstr

	def applyRules(self, char):
		'''
		Checks a character from the current string against the rules and replaces it if necessary
		Paramlist: char (The current character being tested from the current string iteration)
		Return: newchar (The string to be added to the new string. Either the original character if it did not have a rule or the appropriate substitution if the character did have a rule)
		'''
		newchar = ''
		for key in self.rules:
			if char == key:
				newchar = self.rules[key]
				break
			else:
				newchar = char
		return newchar

	def drawCurve(self):
		'''
		Draws the L System based on the final iteration of the string created after applying the rules
		Paramlist: none
		Return: none
		'''
		mike = turtle.Turtle()
		wn = turtle.Screen()
		mike.speed(10)
		for i in range(len(self.orders)):
			if self.orders[i] == "F":
				mike.forward(5)
			elif self.orders[i] == "+":
				mike.right(self.angle)
			elif self.orders[i] == "-":
				mike.left(self.angle)
		mike.clear()
