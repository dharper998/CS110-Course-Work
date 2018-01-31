a = [1, 2, 3]
a.append("apple")
a.append(76)
a.insert(3, "cat")
a.insert(0, 99)
print(a)
print(a.count(76))
for i in range(len(a)):
    if a[i] == 76:
        del a[i]
        break
print(a)
for i in range(len(a)):
    if a[i] == "apple":
        a[i] = "orange"
print(a)

def sum_of_squares(xs):
    sum = 0
    for i in range(len(xs)):
        xs[i] = xs[i]**2
        sum += xs[i]
    print(sum)
sum_of_squares([1, 2, 3])
