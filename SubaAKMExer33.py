import math
list1 = []
list2 = []

n = int(input("How many numbers N are to follow?:\n"))

for i in range(1, n+1):
    num = float(input("Enter the integer:\n"))
    list1.append(num)
    ave1 = (sum(list1)/n)

    num2 = num * num
    list2.append(num2)
    ave2 = (sum(list2)/n)

ave3 = ave1 * ave1

standard_dev = math.sqrt(ave2 - ave3)

print("The standard deviation is: ", standard_dev)