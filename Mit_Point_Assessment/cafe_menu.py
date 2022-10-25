#!/usr/bin/env python3

if __name__ == '__main__':
    num_spam = int(input("How many slices of spam?"))
    txt_1 = " Spam"
    txt_2 = " Spam,"
    txt_3 = " and"
    if num_spam == 1:
        print(f"Egg with{txt_1} coming up!")
    elif num_spam > 1:
        print("Egg with" + txt_2*(num_spam-1) + txt_3 + txt_1 + " coming up!")
    else:
        print("Invalid input")
