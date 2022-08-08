yob = int(input("Year of birth:\n"))
cy = int(input("Current year:\n"))
if cy != 00:
    year = cy - yob
    print("Your age is", year)
elif cy >= 0o1 or cy <= 99:
    year = cy - 100
    print("Your age is", year)
