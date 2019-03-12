a = []
b = []

x = int(input("Enter value of x: "))
deg = input("Enter the degree: ")

for i in range(int(deg) + 1):
    a.append(input("Coefficient by x^" + str(i) + ": "))

a.reverse()
b.append(a[0])

for i in range(int(deg) + 1):
    if i > 0:
        b.append(x * int(b[i - 1]) + int(a[i]))

print(a)
print(b)
print("Value for x = " + str(x) + ": " + str(b[int(deg)]))
