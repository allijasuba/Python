num = ()
totalnumber = ()
n = ()
sum = 0
num = int(input("How many integers will be added:\n"))

while num > 0:
    n = (int(input("Enter an integer:\n")))
    sum = sum + n
    num = num - 1

print("The Sum is", sum)
