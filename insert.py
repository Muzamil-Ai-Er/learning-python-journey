#insert()
#this method is used to insert an object or value at the given index.
#syntax= list.insert(index,object)
#example
a=[5,"ram",10]
a.insert(2,"shyam")
print(a)
#Another example 
print("Another example")
a=[]
for i in range(5):
    x=input("Enter value:")
    a.append(x)
print("Original list is:",a)
index=int(input("Enter index where you want to insert:"))
value=input("Enter value to insert:")
a.insert(index,value)
print("List after insertation:",a)