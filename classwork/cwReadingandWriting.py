def main():
    cipher = 3
    filename = input("Please enter a file name: ")
    fptr = open(filename, 'r')
    encfptr = open(filename + '.enc', 'w')
    file_text = fptr.read()
    enc_text = ""
    for c in file_text:
        if c.isalnum():
            ordnum = ord(c)
            ordnum += cipher
            enc_text += chr(ordnum)
        else:
            enc_text += c
    fptr.close()
    encfptr = open(filename + '.enc', 'w')
    encfptr.write(enc_text)
main()
