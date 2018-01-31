# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
	'''
	Returns the number of donuts if the input is less than 10 and otherwise returns that there are many donuts.
	paramlist: count(the given number of donuts)
	return: string (If count is less than 10: "Number of donuts: count". If count is 10 or greater: "Number of donuts: many")
	'''
	return(("Number of donuts: " + str(count)) if (count < 10) else ("Number of donuts: many"))


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
	'''
	Returns a string consisting of the first two and last two characters of a given string if its length is 2 or greater, otherwise returns an empty string
	paramlist: s (a given string)
	return: string (If the length of s is 2 or greater, returns a string of the first two characters of 2 and the last two characters of s. Otherwise returns an empty string)
	'''
	return(((str(s[0]) + str(s[1]) + str(s[-2]) + str(s[-1])) if len(s) >= 2 else ""))


# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
	'''
	Returns a given string with all instances of its first character replaced by asterisks except for the first character
	paramlist: s (a given string of length 1 or more)
	return: string (String s with all characters that are duplicates of the first replaced by asterisks, not including the first character)
	'''
	return(str(s[0]) + str(s[1:].replace(str(s[0]), str("*"))))


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
	if got == expected:
        	prefix = ' OK '
	else:
        	prefix = '  X '
	print(prefix," got: ", got," expected: ", expected)


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
	print('donuts')
    # Each line calls donuts, compares its result to the expected for that call.
	test(donuts(4), 'Number of donuts: 4')
	test(donuts(9), 'Number of donuts: 9')
	test(donuts(10), 'Number of donuts: many')
	test(donuts(99), 'Number of donuts: many')

	print('both_ends')
	test(both_ends('spring'), 'spng')
	test(both_ends('Hello'), 'Helo')
	test(both_ends('a'), '')
	test(both_ends('xyz'), 'xyyz')

	print('fix_start')
	test(fix_start('babble'), 'ba**le')
	test(fix_start('aardvark'), 'a*rdv*rk')
	test(fix_start('google'), 'goo*le')
	test(fix_start('donut'), 'donut')

main()
