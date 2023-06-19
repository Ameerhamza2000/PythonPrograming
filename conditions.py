# conditions contain blocks of code and sequence is according to indentation
print("Enter name:")
name=input()
print("Enter Password:")
password=input()

if name=='marry':
    print("Welcome Marry!")

    if password=='marry123':
        print("Access Granted")
    
    else:
        print("Not granted")

elif name=='hamza':
    print("hello",name,"!")
else:
    print("Enter correct name")