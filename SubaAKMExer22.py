noi = int(input("Enter the number of items to be heated: "))
time = float(input("Enter time in seconds: "))

if noi == 1:
    print("The recommended heating time is " + str(time))
if noi == 2:
    rt = time + (0.5 * time)
    print("The recommended heating time is '+ str(recommended_Time) +' seconds.")
if noi == 3:
    rt = 2 * time
    print("The recommended heating time is ' + str(recommended_Time)+' seconds.")
if noi > 3:
    print("Heating more than three items at once is not recommended.")

