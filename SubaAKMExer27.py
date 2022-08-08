rfp = float(input("Input right front pressure:\n"))
lfp = float(input("Input left front pressure:\n"))
rrp = float(input("Input right rear pressure:\n"))
lrp = float(input("Input left rear pressure:\n"))

if 45 >= rfp >= 35 and 45 >= lfp >= 35 or 45 >= rrp >= 35 and 45 >= rrp >= 35:
    f = rfp % lfp
    r = rrp % lrp

    if f != 0 and not 1 and not 2 and (not 3 or r != 0) and not 1 and not 2 and not 3:
        print("Inflation is NOT ok")
    else:
        print("Inflation is OK")
else:
        print("Inflation is NOT ok")
