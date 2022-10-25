#!/usr/bin/env python3

if __name__ == '__main__':
    while True:
        password_input = input("Greetings! What is the password? ")
        if password_input == "parrot":
            print("Correct! You may enter.")
            break
        else:
            print("Incorrect! You may try again.")
