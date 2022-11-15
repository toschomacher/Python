#!/usr/bin/env python3

import sys


def list_process(expect_list):

    from re import sub
    ucas_list, temp_list, first_names_list, surnames_list, names_initials = ([] for i in range(5))
    temp_string = ""

    for k in expect_list:
        ucas_list.append(k[:8])
        temp_list.append(k[9:])

    for m in temp_list:
        surnames_list.append(m[:m.index(",")])
        first_names_list.append(m[m.index(",")+1:])

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
            print_list = []

            for n in range(len(my_tuple[0])):
                print_list.append(my_tuple[0][n] + " " + my_tuple[2][n] + my_tuple[1][n] +
                                  number_generator() + "@poppleton.ac.uk")

            with open('students_emails.txt', 'w') as f:
                for b in range(len(print_list)):
                    f.write(str(print_list[b]) + '\n')

            my_file.close()
        except FileNotFoundError:
            print('Error: Cannot open "' + sys.argv[1] + '". Sorry about that.')
