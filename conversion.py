#variable are of int float string
#type conversion int() float() str()
print(int('9')+5)
print(float('9.5')+5)

#concatination 
print('9'+str(5))

print(int(7.7))

print('you are '+str(99)+' years old')

print(42=='42') #false
print(42==42.0) #true
#This will throw error because int() cant evaluate floating in string
print(int('9.5'))