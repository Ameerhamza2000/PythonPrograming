lines=int(input("how many lines you want to print:"))

spaces=lines
for i in range (1,lines+1):
    for j in range(spaces):
        print(" ",end="")
    
    for k in range (2*i-1):
        print("*",end="")
        
    
    spaces=spaces-1
    print("")
    

spaces=1
for i in range(lines,0,-1):
    for j in range(spaces):
        print(" ",end="")
    
    for k in range(2*i-1):
        print("*",end="")
    
    spaces=spaces+1
    print("")


