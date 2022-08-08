Tair = float(input("Enter the air temperature in K:\n"))
Tstream = float(input("Enter the steam temperature in K:\n"))
e = 1 - Tair / Tstream
if Tstream >= 373:
    print("Steam Engine Efficiency is", e)
elif Tstream < 373:
    print("Steam Engine Efficiency is zero")
