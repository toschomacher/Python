#!/usr/bin/env python3

from random import randrange

if __name__ == "__main__":
    LIST_ONE = ["one","two","three","four","five","six","seven","eight"]
    LIST_TWO = ["Alex","Benji","Caren","David","Emily","Frank","George","Hudson"]
    LIST_THREE = ["Zunisha","Yellow","Xylophone","White","Violet","Unicorn","Turquoise","Silver"]
    
    print("Password Generator\n==================")
    
    while True:
        try:
            number_passwords = int(input("How many passwords are needed?:"))
            if 0 < number_passwords < 25:
                break
            else:
                print("Please enter a value between 1 and 24.")
        except ValueError:
            print("Please enter a number.")
            
    for n in range(number_passwords):
        new_password = LIST_ONE[randrange(7)]+LIST_TWO[randrange(7)]+LIST_THREE[randrange(7)]
        print(f"{n+1} --> " + new_password)
    
