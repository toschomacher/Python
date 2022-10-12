#!url/bin/env python3

if __name__ == '__main__':
    # Task 1
    name = input("Enter your name: ")
    if not name:
        print('Hello stranger')
    elif not str. isupper(name[0]):
        print('Did you mean ' + name[0].upper() + name[1:] + '?')
    else:
        print('Hello', name)

    # Task 2
    print('\n*********** Task 2 ***********')
    password = input('Please enter a new password: ')
    password_verify = input('Please re-enter the password:')
    if password == password_verify:
        print("Password Set")
    else:
        print("Error: Passwords do not match.")

    # Task 3
    print('\n*********** Task 3 ***********')
    password = input('Please enter a new password between 8 and 12 characters: ')
    if 7 < len(password) < 13:
        password_verify = input('Please re-enter the password:')
        if password == password_verify:
            print("Password Set")
        else:
            print("Error: Passwords do not match.")
    else:
        print("Error: Password must be between 8 and 12 characters.")

    # Task 4
    print('\n*********** Task 4 ***********')
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    password = input('Please enter a new password between 8 and 12 characters: ')
    if 7 < len(password) < 13:
        if password not in BAD_PASSWORDS:
            password_verify = input('Please re-enter the password:')
            if password == password_verify:
                print("Password Set")
            else:
                print("Error: Passwords do not match.")
        else:
            print(f"Password can not contain the word {password}")
    else:
        print("Error: Password must be between 8 and 12 characters.")

    # Task 5
    print('\n*********** Task 5 ***********')
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    while True:
        count = 0
        password = input('Please enter a new password between 8 and 12 characters: ')
        if 7 < len(password) < 13:
            if password not in BAD_PASSWORDS:
                password_verify = input('Please re-enter the password:')
                if password == password_verify:
                    print("Password Set")
                    break
                else:
                    print("Error: Passwords do not match.")
            else:
                print(f"Password can not contain the word {password}")
        else:
            print("Error: Password must be between 8 and 12 characters.")

    # Task 6
    print('\n*********** Task 6 ***********')
    print('\tSeven Time Table:')
    print(' __________________________________')
    print('|Opera- | Multi-| Multi- | Result/|')
    print('|tion # |plicand| plier  | Product|')
    print('|_______|_______|________|________|')
    
    count = 1
    multiplicand = 7
    
    for mult in range(13):
        print(f'|{count:2}', f'\t|  {multiplicand}', '   x', f'  {mult}', '\t =  ', f'{mult*multiplicand:2}', '  |')
        count +=1
    
    print('|_______|_______|________|________|')
    
    # Task 7
    print('\n*********** Task 7 ***********')
    print('\tChoose A Time Table:')
    
    count = 1
    multiplicand = int(input('Choose a multiplicand from 0 to 12: '))
    
    print(' ___________________________________')
    print('|Opera- | Multi-| Multi- | Result/ |')
    print('|tion # |plicand| plier  | Product |')
    print('|_______|_______|________|_________|')
    
    for mult in range(13):
        print(f'|{count:2}', f'\t|  {multiplicand:2}', '  x', f'  {mult:2}', '  =  ', f'{mult*multiplicand:3}', '  |')
        count +=1
        
    print('|_______|_______|________|_________|')
    
    # Task 8
    print('\n*********** Task 8 ***********')
    print('\tChoose A Time Table:')
    
    while True:
        multiplicand = int(input('Choose a multiplicand from -12 to +12: '))
        if 0 <= multiplicand < 13:
            break
        elif -13 < multiplicand < 0:
            break
        else:
            print('Error: Invalid number.\nEnter a number between -12 and 12 inclusive.')
    print(' ___________________________________')
    print('|Opera- | Multi-| Multi- | Result/ |')
    print('|tion # |plicand| plier  | Product |')
    print('|_______|_______|________|_________|')
    
    start_range = 0
    finish_range = 13
    count = 1
    
    if multiplicand <0:
        multiplicand *=-1
        start_range = -12
        finish_range = 1
    
    for mult in range(start_range,finish_range):
        mult = mult * -1
        print(f'|{count:2}', f'\t|  {multiplicand:2}', '  x', f'  {mult:2}', '  =  ', f'{mult*multiplicand:3}', '  |')
        count +=1
    
    print('|_______|_______|________|_________|')
    
