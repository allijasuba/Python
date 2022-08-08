shipping = 2.00
a = 5.00
sum = 0

i = input("Please enter the item:")
p = int(input("Please enter the price:"))
d = int(input("Overnight delivery (0==no, 1==yes):"))
cp = p / 100

if cp < 10:
    shipping = 2.00
if cp >= 10:
    shipping = 3.00
if d == 1:
    shipping += 5.00
sum = cp + shipping
print("Invoice")
print(str(i) + ': ' + str(cp))
print("Delivery", shipping)
print("Total", sum)
