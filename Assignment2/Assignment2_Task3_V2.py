#!/usr/bin/env python3

import sys


def list_process(expect_list):

    from re import sub
    names_initials = []
    temp_string = ""

    ucas_list = [k[:8] for k in expect_list]
    temp_list = [k[9:] for k in expect_list]
    surnames_list = [k[:k.index(",")] for k in temp_list]
    first_names_list = [k[k.index(",")+1:] for k in temp_list]
    surnames_list = [element.lower() for element in surnames_list]

    for x in surnames_list:
        new_string = sub(r'[^a-zA-Z]', '', x)
        surnames_list[surnames_list.index(x)] = new_string

    for element in first_names_list:
        for c in range(0, len(element)):
            if element[c] == ' ':
                temp_string += element[c+1].lower() + '.'
            if c == len(element)-1:
                names_initials.append(temp_string)
                temp_string = ""

    return ucas_list, surnames_list, names_initials


def number_generator():

    from random import randint
    rand_number = ""
    for num in range(4):
        rand_number += str(randint(0, 9))

    return rand_number


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Error: Missing command-line argument.")
    else:
        try:
            my_file = open(f"{sys.argv[1]}", "r")
            my_tuple = list_process(my_file.readlines())
            print_list = [(my_tuple[0][n] + " " + my_tuple[2][n] + my_tuple[1][n] + number_generator() +
                           "@poppleton.ac.uk") for n in range(len(my_tuple[0]))]

            with open('students_emails.txt', 'w') as f:
                for b in range(len(print_list)):
                    f.write(str(print_list[b]) + '\n')

            my_file.close()
        except FileNotFoundError:
            print('Error: Cannot open "' + sys.argv[1] + '". Sorry about that.')
