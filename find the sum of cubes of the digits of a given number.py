i=int(input("Enter the number:"))
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
print("The sum of the cubes of the digits=",sum)