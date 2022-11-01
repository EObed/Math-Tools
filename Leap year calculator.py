year = int(input("Which year would you want to check?\n"))
if year%4==0:
    if year%100!=0:
        print("The year " +str(year)+ " is a leap year")
        if year%400==0:
            print("The year " +str(year)+ " is a leap year")
    else:
            print("The year " +str(year)+ " is not a leap year")
else:
    print("The year " +str(year)+ " is not a leap year")