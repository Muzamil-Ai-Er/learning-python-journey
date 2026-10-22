a=[]
size=int(input("Enter size of the list:"))
for i in range(size):
    val=int(input("Enter Number:"))
    a.append(val)
min=a[0]
for i in range(size):
    if(a[i]<min):
        min=a[i]
print("Min Number=",min)