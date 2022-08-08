sum = 0
sum_1 = 0
d = ()

low = float(input("Low end of range:\n"))
high = float(input("High end of range:\n"))
while d != 0:
    d = int(input("Enter data:\n"))
    if low <= d >= high:
        sum = sum + d
    else:
        sum_1 = sum_1 + d

print("Sum of in range values: ", sum_1)
print("Sum of out of range values:", sum)