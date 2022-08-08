pressureisfine = True

rfp = float(input('Input right front pressure:\n '))
if rfp not in range(35, 45):
    print("Warning: pressure is out of range")
    pressureisfine = False
lfp = float(input('Input left front pressure:\n '))
if lfp not in range(35, 45):
    print("Warning: pressure is out of range")
    pressureisfine = False
rrp = float(input('Input right rear pressure:\n '))
if rrp not in range(35, 45):
    print("Warning: pressure is out of range")
    pressureisfine = False
lrp = float(input('Input left rear pressure:\n '))
if lfp not in range(35, 45):
    print("Warning: pressure is out of range")
    pressureisfine = False

if rfp == lfp and rrp == lrp and pressureisfine == True:
    print("Inflation is OK.")
if rfp != lfp or rrp != lrp or pressureisfine == False:
    print("Inflation is BAD.")
