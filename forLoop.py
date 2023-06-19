#for loop is more concise and used for counted number of times
# for i in range(till number here)
# range use one argument range(5) it loops for 5 times 
# range also use two arguments range(1,6) start and ending number 
# range also uses three arguments range(0,10,2) third one is increment in number

#one argumentr
for i in range(5):
    print("Hello",i)

print("\nUsing two arguments\n")

for i in range(10,15):
    print("(",i,")")

print("\nUsing three arguments\n")

for i in range(1,20,2):
    print(i)

print("\nDecrement\n")
for i in range(10,0,-1):
    print(i)

print("\nNested Loop\n")
for i in range(5):
    for j in range(5):
        print(i)