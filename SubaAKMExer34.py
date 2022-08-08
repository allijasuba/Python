import math

n = int(input("Upper Limit:\n"))
sum = 0
sum_1 = 0

while n > 0:
    sum = sum + math.pow(n, 2)
    sum_1 = sum_1 + math.pow(n, 3)
    n = n - 1

print("The sum of Squares is:", int(sum))
print("The sum of cubes is:", int(sum_1))
