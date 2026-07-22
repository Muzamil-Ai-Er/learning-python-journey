i=int(input("Enter the number to find sum of square of digits:"))
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)
    i=i//10
print("Sum of square of each digits=",sum)