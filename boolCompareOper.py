# Comparison operators also known as realtional operators used 
# to comapre two values which returns True or False
# == , < , > , <= ,>= ,!=

print('Comparison Operators Rsults')

spam = 2==2
print('1 : ',spam)

spam = 2<3
print('2 : ',spam)

spam = 2>3
print('3 : ',spam)

spam = 2<=2
print('4 : ',spam)

spam = 3>=2
print('5 : ',spam)

spam= 2!=2
print('6 : ',spam)
# print('\n')

#Boolean Operators are " and , or , not "
print ('\nBoolean Operators Results')

print ('1 :', True and True)
print ('2 :', True and False)
print ('3 :', False and True)
print ('4 :', False and False)

print ('5 :',False or False)
print ('6 :',False or True )

#not is unary operator
print('7 :', not True)
print('8 :', not False )

print('9 :', not not not True)

#Mixing Boolean and Comparison Operators
print('\nBoolean and Comparison Operators Results')

print ((4<5) and (3>=3))
print ((4>5) or (5==5))
print (not(4>5) and (5==5))