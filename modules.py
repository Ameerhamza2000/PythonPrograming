# from random import*
#you can import built in functions of python to perform different tasks random , sys , os , math etc
# import random 
# remember to not make the files name same as modules of pyhton then it will import function from your that one file
import random, sys

for i in range(5):
    print(random.randint(1,10))

while True:
    print("Enter exit or you name")
    name=input()
    if name=='exit':
        sys.exit()