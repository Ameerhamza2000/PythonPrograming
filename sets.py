# sets are collection of data stores different data types
# sets have no index,unchangeable and no duplication
# but you can add or remove elements from sets
# set() constructor use to make a set
# {} represents sets
# true and 1 indicates true

myset={1,2,3,"hello","fruits",False}

print(myset)

# you can add a item
myset.add("newitem")
print(myset)

# remove is used to remove a item but it returns error if no item found
myset.remove(False)

# discard also use to remove a item without any error
myset.discard(1)
print(myset)

# you can clear a set
myset.clear()
print(myset)

# delete a whole set
# del myset
# print(myset)

# loop through set
set1=set((1,2,3))
for i in set1:
    print(i)
    
# Joining two sets
# if you use union to join it returns values in a new set
set1={1,2,3,"banana","orange","hello"}
set2={2,4,5,1,"orange"}

set1.update(set2)
print(set1)

# can get only common in both sets
# if use only intersection it returns value into a new set set3
set1={1,2,3,"banana","orange","hello"}
set2={2,4,5,1,"orange"}

set1.intersection_update(set2)
print("Intersection Update",set1)

# can discard the common values in both sets
set1={1,2,3,"banana","orange","hello"}
set2={2,4,5,1,"orange"}

set1.symmetric_difference_update(set2)
print("Symmetric diffrence",set1)

# diffrence gives values in set 1 that are not in set2
set1={1,2,3,"banana","orange","hello"}
set2={2,4,5,1,"orange"}

set1.difference_update(set2)
print("Differ update",set1)