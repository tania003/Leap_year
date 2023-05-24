year =int(input("Enter the year :  "))
m = year%4
if m == 0:
    print("this is a leap year")
else:
    print("not a leap year")