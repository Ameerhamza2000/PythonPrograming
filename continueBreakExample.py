# if you entered wrong name or wrong password this program will ask you to enter correct input according to field you entering

name='' 
password=''

while True:
    print("Enter your name")
    name=input()

    # loop for asking correct name again and again
    while name !='joe':
            print("Wrong name! Renter your name again")
            name=input()

            if name !='joe':
                continue

    
    print("enter your password")
    password=input()

    # loop for asking correct password again and again
    while password !='joe123':
        print("Wrong Password!Renter your password again")
        password=input()

        if password !='joe123':
            continue

    if password =='joe123':
        break     