# lists contains multiple values (strings,numbers,floating numbersboolean at the same time)starts and ends with a square bracket 
# values in a lists are called items separated by commas

animals=['cat','dog','wolf',2,3.15,True,False,None]

print(animals)

print("hello ",animals[2])

# a list can contain another list which will be accesible with multiple indexis
multiList=[['cat','dog',2],5,7.8,[1,2],'hello world']

print(multiList[0][1])
print(multiList[1])
print(multiList[3][0])
print(multiList[4])

# lists can also be accesed with negative indexes -1 indicates last item
print(animals[-1])
print(animals[-6])
print(animals[-8])

# negative indexing in multiple lists
print(multiList[-1])
print(multiList[-2])
print(multiList[-2][-1])