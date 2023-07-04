# there is a local scope and global scope if a variable is outside of a function it is in global cope
# but in a function variable has the local scope 

def test():
    scope = "local"
    print(scope)

scope="global"
test()

print(scope)

# if there will no assignment of a variable in a function with same name of global then it is acceses as global
def test2():
    print(scope2)

scope2="global"
test2()

# if you want to access the same global variable in function global is required at the top of function

def test3():
    global scope3
    scope3 = "local"

scope3="global"
test3()
print("scope3 ",scope3)