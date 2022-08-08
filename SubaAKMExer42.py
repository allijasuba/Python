import months as months

balance = 1000
interest = .015
times = 0
pay = 0
monthly = float(input("Enter the monthly payment:\n"))


def total(args):
    pass


while balance >= 0:
    months =+ 1
    c = balance * interest
    debt = (balance - monthly) + c
    times = times +1
    pay = pay + monthly
    print("Month:", total, "balance:", debt,  "total payments:", pay)
total = pay + debt
print("Total payments:, total ")
