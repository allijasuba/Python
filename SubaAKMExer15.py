
bp = 5
np = 3
wp = 1


b = int(input("Please enter the number of bolts:\n"))
n = int(input("Please enter the number of nuts:\n"))
w = int(input("Please enter the number of washers:\n"))


if b >= n:
    print("Check the Order")
else:
    print("Order is OK")
t = b * bp + n * np + w * wp
print("Total cost:", t)
