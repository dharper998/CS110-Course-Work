import random

def encrypt(text):
	'''
	Takes a string from the user, creates a cipher, and encrypts the string based on the cipher
	Paramlist: text (a string inputted by the user)
	return: A tuple of encryptstr (the string created after encrypting the original string) and dictionary (the cipher)
	'''
	chars = []
	for i in range(32, 127):
		chars += [chr(i)]
	dictionary = {}
	for i in range(32, 127):
		randomchar = random.choice(chars)
		dictionary[chr(i)] = randomchar
		chars.remove(randomchar)
	encryptstr = ""
	for i in text:
		encryptstr += dictionary[i]
	print(encryptstr)
	return (encryptstr, dictionary)

def decrypt(text, cipher):
	'''
	Takes the encrypted string and decrypts it back to the original string
	Paramlist: text (the encrypted string), cipher (the cipher dictionary)
	return: decryptstr (the string created after decrypting the encrypted string, equal to the original string)
	'''
	decryptstr = ""
	for i in text:
		for c in cipher:
			if cipher[c] == i:
				decryptstr += c
	print(decryptstr)
