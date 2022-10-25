#!/usr/bin/env python3

if __name__ == '__main__':
    user_input = input("Greetings! How shall we call you?")
    check_list = user_input.split()
    if check_list[0] == "Lord" or check_list[0] == "Lady":
        print(f"It shall be so, {user_input}!")
    else:
        print("You may not be known by that name!")
