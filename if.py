print(">>>>>>>>>Program to find a middle number in a group of three numbersaa<<<<<<")
a=int(input("Enter your fist number:"))
b=int(input("Enter your second number:"))
c=int(input("Enter your third number:"))
if (a>b and a<c) or (a<b and a>c):
    print("The middle number=",a)
elif (b>a and b<c) or (b<a and b>c):
    print("The middle number=",b)
else:
    print("The middle number=",c)