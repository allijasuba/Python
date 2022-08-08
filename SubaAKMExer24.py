checking_acc = float(input("Enter the money in your checking account:\n"))
savings_acc = float(input("Enter money in savings acc:\n"))

if checking_acc < 1000 and savings_acc < 1500:
  print("Service charge is $0.15 per check.")
else:
  print("Service Charge is free.")
