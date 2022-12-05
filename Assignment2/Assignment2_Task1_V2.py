#!/usr/bin/env python3


def password_generator():
    from random import randrange
    from constants import WORDS
    count = 0
    password_data = []
    while count < passwords_required:
        new_password = WORDS[randrange(0, 8)] + WORDS[randrange(8, 16)] + WORDS[randrange(16, 24)]
        if new_password not in password_data:
            password_data.append(new_password)
            print(f"{count + 1:<2d} --> " + new_password)
            count += 1


def user_interaction():
    while 1:
        try:
            number_of_passwords = int(input("How many passwords are needed?: "))
            if 0 < number_of_passwords < 25:
                break
            else:
                print("Please enter a value between 1 and 24.")
        except ValueError:
            print("Please enter a whole number.")
    return number_of_passwords


if __name__ == "__main__":
    print("Password Generator\n==================")
    passwords_required = user_interaction()
    password_generator()
