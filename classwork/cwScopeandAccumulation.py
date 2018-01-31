def mult(x, y):
    accum = 0
    for i in range(x):
        accum = accum + y
    return accum

def exp(x, y):
    accum = 1
    for i in range(y):
        accum = accum * x
    return accum

def square(num):
    return mult(num, num)

def main():
    x = 5
    y = 3
    num = mult(x, y)
    result1 = mult(x, y)
    result2 = exp(x, y)
    result3 = square(num)
    print(result1)
    print(result2)
    print(result3)
main()
