#remove(obeject)
#This method is used   to delete on object/value from the given list. note that it  removes/deletes the first occurance of the list.
#syntax = list.remove(object)
# example
a=["ram",10,"ravi",5,10]
a.remove(10)
print(a)
print("project with users input usuing remove list")

a=[]
for i in range(5):
    x=input("Enter value:")
    a.append(x)
print("original list=",a)
val=input("Enter value to remove:")
a.remove(val)
print("List after removing the given value:",a)