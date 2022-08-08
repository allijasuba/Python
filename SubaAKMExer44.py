import math

print("e^x\n")

x = int(input("enter x: "))
print()
n = 0
sum = 1
term = 1

while term > 1.0E-12:
    n += 1
    term = (x**(n-1)/math.factorial(n-1)) * x/n
    sum += term
    print("n:", n, "term:", term, "Sum:", sum)
else:
    print("my e^x:", sum)
