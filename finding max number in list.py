a=[]
size=int(input("Enter size of the list:"))
for i in range(size):
    val=int(input("Enter Number:"))
    a.append(val)
max=a[0]
for i in range(size):
    if(a[i]>max):
        max=a[i]
print("Max Number=",max)