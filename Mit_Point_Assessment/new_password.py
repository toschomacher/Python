#!/usr/bin/env python3

def password_checker(password):
    from string import ascii_letters as letters, digits, punctuation
    has_letter = has_digit = has_punc = False
    for character in password:
        if character in letters:
            has_letter = True
        elif character in digits:
            has_digit = True
        elif character in punctuation:
            has_punc = True
    return has_letter and has_digit and has_punc


if __name__ == '__main__':
    print("Please create a new password.\nThe password must contain at least one letter,"
          " at least one digit, and at least one standard punctuation character..")
    user_input = input("Enter password: ")
    if password_checker(user_input):
        print("Password is acceptable!")
    else:
        print("Password is not acceptable!")
