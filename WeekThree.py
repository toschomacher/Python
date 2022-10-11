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
    password_verify = input('Please enter the password again:')
    if password == password_verify:
        print("Password Set")
    else:
        print("Error: Passwords do not match.")

    # Task 3
    print('\n*********** Task 3 ***********')
    password = input('Please enter a new password between 8 and 12 characters: ')
    if 7 < len(password) < 13:
        password_verify = input('Please enter the password again:')
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
            password_verify = input('Please enter the password again:')
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
                password_verify = input('Please enter the password again:')
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
    print()
