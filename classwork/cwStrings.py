def loop():
    stringone = ""
    for i in range (1, 1000):
        stringone = stringone + str(i) + ", "
    stringone += "1000"
    print(stringone)

def binghamton():
    bingstring = "Binghamton"
    bingstring1 = bingstring[:3]
    bingstring2 = bingstring[4:6] + bingstring[7]
    bingstring3 = bingstring[:2] + bingstring[7] + bingstring[1:4]
    print(bingstring1 + ", " + bingstring2 + ", " + bingstring3)

def function3():
    results = 'average: 0.8475'
    colonindex = results.find(":")
    value = results[colonindex+1:].strip()
    floatvalue = float(value)
    print(floatvalue)

def main():
    loop()
    binghamton()
    function3()
main()
