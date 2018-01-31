def value(portfolio):
    maximum = (portfolio[0][1], portfolio[0][3])
    for i in portfolio:
        purchprice = i[0]
        shares = i[1]
        symbol = i[2]
        currprice = i[3]
        valuegain = ((shares * currprice) - (purchprice * shares))
        if valuegain > maximum[1]:
            maximum = (symbol, valuegain)
    return maximum

def main():
    portfolio = [(43.50, 37, 'APL', 92.45), (32.80, 50, 'TYT', 51.19), (52.10, 22, 'GGL', 34.87)]
    print(value(portfolio))
main()
