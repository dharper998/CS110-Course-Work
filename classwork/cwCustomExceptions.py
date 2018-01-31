class WrongAnswerError(Exception):
    pass

class NoAnswerError(Exception):
    pass

def main():
    food = input("What is your favorite food?")
    try:
        if food == "":
            raise NoAnswerError()
        elif food != "Pancakes":
            raise WrongAnswerError()
    except NoAnswerError:
        print("Pancakes")
    except WrongAnswerError:
        print("Wrong, the correct answer is Pancakes")
    else:
        print("You have good taste")
main()
