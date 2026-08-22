i=int(input("Enter number:"))
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
print(rev)
if(rev==i):
    print("palindrome number")
else:
    print("Not a palindrome number")