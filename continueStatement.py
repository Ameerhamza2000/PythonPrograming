# whenever execution reaches to Continue statement loop jumps back to the top

name=''

while True:
    print("Enter your name:")
    name=input()
    if name!='joe':
        continue
    else:
        break
    
    # print("hello")
   
        