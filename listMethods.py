# lists are mutable

list1=[4,8,9,10,2,3]
list1.sort()
print(list1)

# descending order

list1.sort(reverse=True)
print(list1)

# list as arguement of function
# it stores as refrence of a list
def listFunction(listRef):
    listRef[0]="bye"
    listRef[1]="world"

list2=["hello","world"]
listFunction(list2)

print(list2)

# copy list
# changes in list3 also changes in list 1
list3=list1
# copy solution
list3=list(list1)
# or
list3=list1.copy()

# to add new value in a list
list4=["hello","fruits","car","bike"]
list4.append("banana")
print(list4)

# to ad a specific index it shifts the existing elements next
list4.insert(2,"mango")
print(list4)

# to delete a element if you know index
del list4[0]
print(list4)

# if you want the value of remove element
remEle=list4.pop(1)
print(list4)
print(remEle)

# if you know value of element
list4.remove("car")
print(list4)


# looping through list
for i in list4:
    print(i,end=" ")

print("\n")
for x in list4:
    print((len(i),x))

# list comprehension
[print(x) for x in list4]