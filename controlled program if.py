print(">>>>>>> verifying whether you are eligible to vote<<<<<<<<<<")
a=int(input("Enter your age:"))
if a>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
print(">>>>>>>>>>Finding the max number between two digits<<<<<<<<<")
a=int(input("Enter you first digit:"))
b=int(input("Enter your second digit:"))
if a>b:
    print("Max number=",a)
else:
    print("Max number=",b)
print(">>>>>>>>Finding Max number between three digits<<<<<<<")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b and a>c:
    print("Max number =",a)
elif b>a and b>c:
    print("Max number=",b)
else:
    print("Max number=",c)
print(">>>>>>>>program to check whether a given number is positive negative or zero<<<<<<<<<")
a=int(input("Enter your number:"))
if a==0:
    print("The given number is zero")
elif a>0:
    print("The given number is positive")
else:
    print("The given number is negative")