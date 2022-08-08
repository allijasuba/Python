tc = int(input("Tank capacity:\n"))
gr = int(input("Gage reading:\n"))
mpg = int(input("Miles per gallon:\n"))

fc = mpg * tc
ac = ((gr/100)*tc)*mpg

if ac >= fc:
    print('Safe to Proceed!')
elif ac < fc:
    print('Get Gas!')
