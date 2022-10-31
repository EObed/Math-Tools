number = int(input("Enter number and hit enter: "))
digit = 2
if number==1:
    print("The first number in the Fibonacci sequence is: 1")
elif number==2:
    print("The first two numbers in the Fibonacci sequnce are: 1 and 1")
elif number>2:
    a = [1, 1]
    while digit < number:
        nextNumber=a[digit-1]+a[digit-2]
        a.append(nextNumber)
        digit+=1
    print("The first" + str(number) + "numbers in the Fibonacci sequence are: " + str(a))      
else:
    print("Invalid entry")