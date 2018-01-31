import math
def main():
    num = input("Please enter a number: ")
    if num.isdigit() and num != 0:
        better_num = 5/int(num) * -1
    else:
        print("This number cannot get any better")

    if better_num >= 0
        even_better_num = math.swrt(better_num)
    else:
        print("This number cannot get any better")
main()


def noError(param):
    i = 0
    try:
        size = len(param)
        while (i < size):
            print(param[i])
            i += 1
    except:
        print(param)
