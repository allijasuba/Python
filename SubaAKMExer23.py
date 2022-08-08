name = input("Please enter the name of your character:\n")
strength = int(input("Enter strength (1-10):\n"))
health = int(input("Enter health (1-10):\n"))
luck = int(input("Enter luck (1-10):\n"))

sum = strength + health + luck

if sum <= 15:
        print("Your character is created")
else:
        print("You have given your character too many points! Default values have been assigned:\n "
              "Chortle, strength: 5, health: 5, luck: 5")
