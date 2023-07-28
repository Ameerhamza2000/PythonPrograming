# Tuples are also data storing like lists 
# it is ordered ,unchangeable,allows duplicate elements
# tuple have not only single elements only possible with (1,)

tuple1=("hey","i","am","tuple")
tuple2=(1,2,3,4)
print(tuple1)

# you can add tuples
tuple3=tuple1+tuple2
print(tuple3)

# tuple() constructor

tuple4= tuple(("fruits",))
print(tuple4)

# if you want to chnage tuple first make it list then apply changes
tuplelist= list(tuple1)
tuplelist[3]="list changes tuple"
# print(tuplelist)
tuple1=tuple(tuplelist)
print(tuple1)

# you can delete whole tuple
del tuple2

# can assign values as tuple variable but as same length of tuple
t=(1,2,3,4,1)
var1,var2,var3,var4,var5=t
print(var4)

# if you dont know length of tuple then use asterik*

a,*b,c=t
print(a)
print(b)
print(c)

# Tuple methods
print(len(t))
print(t.count(1))