#!/usr/bin/env python3

from random import randrange

if __name__ == "__main__":
    LIST_ONE = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
    LIST_TWO = ["Alex", "Benji", "Caren", "David", "Emily", "Frank", "George", "Hudson"]
    LIST_THREE = ["Zunisha", "Yellow", "Xylophone", "White", "Violet", "Unicorn", "Turquoise", "Silver"]

    print("Password Generator\n==================")

    while True:
        try:
            number_passwords = int(input("How many passwords are needed?:"))
            if 0 < number_passwords < 125:
                break
            else:
                print("Please enter a value between 1 and 24.")
        except ValueError:
            print("Please enter a number.")

    new_list = []
    count = 0

    while count < number_passwords:
        new_password = LIST_ONE[randrange(7)] + LIST_TWO[randrange(7)] + LIST_THREE[randrange(7)]
        if (new_password not in new_list):
            new_list.append(new_password)
            print(f"{count + 1} --> " + new_password)
            count += 1
        else:
            print("!DUPLICATE GENERATED:   " + new_password + "   :BUT IGNORED!")
