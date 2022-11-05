#!/usr/bin/env python3

from random import randrange

if __name__ == "__main__":
    LIST_WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight",
                 "Alex", "Benji", "Caren", "David", "Emily", "Frank", "George", "Hudson",
                 "Zunisha", "Yellow", "Xylophone", "White", "Violet", "Unicorn", "Turquoise", "Silver"]
    print("Password Generator\n==================")

    while 1:
        try:
            number_passwords = int(input("How many passwords are needed?: "))
            if 0 < number_passwords < 125:
                break
            else:
                print("Please enter a value between 1 and 24.")
        except ValueError:
            print("Please enter a number.")

    new_list = []
    count = 0

    while count < number_passwords:
        new_password = LIST_WORDS[randrange(0, 8)] + LIST_WORDS[randrange(8, 16)] + LIST_WORDS[randrange(16, 24)]
        if new_password not in new_list:
            new_list.append(new_password)
            print(f"{count + 1} --> " + new_password)
            count += 1
