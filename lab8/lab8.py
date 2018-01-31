import cipher
import random


def main():
	loop = True
	while loop == True:
		inputtext = input("Please enter a string: (q to Quit) ")
		if inputtext == "q":
			print("Goodbye!")
			loop = False
			break
		encrypted = cipher.encrypt(inputtext)
		decryptinput = input("Would you like to decrypt your message?: (y/n)")
		if decryptinput == "y":
			decrypted = cipher.decrypt(encrypted[0], encrypted[1])
			decryptloop = False
		elif decryptinput == "n":
			decryptloop = False
main()
