i=int(input("Enter the number to check if it is an Armstrong number:"))
orig=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("yes")
else:
    print("No")