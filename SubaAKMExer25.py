fp = float(input("Input right front pressure:\n")), float(input("Input left front pressure:\n"))
bp = float(input("Input right rear pressure:\n")), float(input("Input left rear pressure:\n"))

if fp[1] == fp[0] and bp[0] == bp[1]:
        print("Inflation is OK")
else:
        print("Inflation is BAD")
