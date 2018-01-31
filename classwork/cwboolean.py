import random

def main():
    num = random.randrange(1, 11)
    for i in range(3):
        guess = int(input("What do you think the number is?"))
        if(guess > num):
            print("Too High!")
        elif(guess < num):
            print("Too Low!")
        else:
            print("Correct!")
            break
main()
