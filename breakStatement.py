# Whenever program execution reaches break statement execution comes out of loop

name=''

while True:
    print("Enter your name (or enter exit to terminate):")
    name=input()
    
    if name=='exit':
        break