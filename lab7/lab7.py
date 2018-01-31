import lsystems

def main():
	axiom = input("What would you like the axiom to be?: ")
	iterations = int(input("How many iterations would you like to go through?: "))
	angle = int(input("What angle would you like to use?: "))
	distance = int(input("What would you like the distance to be?: "))
	number_of_rules = int(input("How many rules are you applying?: "))
	rules = []
	for i in range(number_of_rules):
		rule = [input("Enter a rule in the format 'character:substitution' : ")]
		rules += rule
	orders = lsystems.createLSystem(iterations, axiom, rules)
	lsystems.drawLSystem(orders, distance, angle)
main()
