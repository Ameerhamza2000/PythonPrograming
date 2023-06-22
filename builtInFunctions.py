# print()
print('Enter your name :')

# input() always take input as string if you enter a number then conversion is required
myName = input()

print('Enter your age :')
myAge = int(input())

# type()
print(type(myName))
print(type(myAge))

# round() to round a number
x=round(5.42314)
print(x)
y = round(5.55646,2)
print(y)

# absolute value which converts negative values into positive like lengths which are never negative
length1= -18.5
print(abs(length1))

# power of something
number=2
print(pow(number,4))