a = float(input('Price per pound package A: \n'))
a1 = float(input('Percent lean package A: \n'))
b = float(input('Price per pound package B: \n'))
b1 = float(input('Percent lean package B: \n'))
cost_A = a/(a1/100)
cost_B = b/(b1/100)

print("Package A cost per pound of lean:", cost_A)
print("Package B cost per pound of lean:", cost_B)

if cost_A < cost_B:
    print('Package A is the best value.')
elif cost_B < cost_A:
    print('Package B is the best value.')
