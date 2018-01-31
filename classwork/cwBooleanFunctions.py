def grade():
    percent = int(input("What was the exam score percentage?"))
    if percent >= 90:
        return "A"
    elif percent >= 80:
        return "B"
    elif percent >= 70:
        return "C"
    elif percent >= 60:
        return "D"
    elif percent < 60:
        return "F"

def isPassing(lettergrade):
    return lettergrade in ['A', 'B', 'C']

def main():
    lettergrade = grade()
    if isPassing(lettergrade):
        print("You Passed")
    else:
        print("You Failed")
main()
