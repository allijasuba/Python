x = int(input("Please enter a number:\n"))
dollar = x // 100
a = x % 100
quarter = a // 25
b = a % 25
dime = b // 10
c = b % 10
cent = c // 1
print(dollar)
print("Your change is", dollar, "dollar/s", quarter, "quarter/s", dime, "dime/s", cent, "cent/s")
