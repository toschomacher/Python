#!/usr/bin/env python3

def list_process(expect_list):
    from re import sub as replace
    names_initials = []
    temp_string = ""
    ucas_list = [k[:8] for k in expect_list]
    temp_list = [k[9:] for k in expect_list]
    surnames_list = [k[:k.index(",")] for k in temp_list]
    first_names_list = [k[k.index(",")+1:] for k in temp_list]
    surnames_list = [element.lower() for element in surnames_list]
    for x in surnames_list:
        new_string = replace(r"[^a-zA-Z]", "", x)
        surnames_list[surnames_list.index(x)] = new_string
    for element in first_names_list:
        for c in range(0, len(element)):
            if element[c] == " ":
                temp_string += element[c+1].lower() + "."
            if c == len(element)-1:
                names_initials.append(temp_string)
                temp_string = ""
    return ucas_list, surnames_list, names_initials


def four_digits():
    from string import digits
    from random import choice
    return ''.join([choice(digits) for _ in range(4)])


def final_format(data_tuple):
    return [(data_tuple[0][n] + " " + data_tuple[2][n] + data_tuple[1][n] + four_digits() +
             "@poppleton.ac.uk") for n in range(len(data_tuple[0]))]


def write_file(print_list):
    with open("students_emails.txt", "w") as f:
        for b in range(len(print_list)):
            f.write(str(print_list[b]) + "\n")


if __name__ == "__main__":
    from sys import argv as file
    file_name = file[1]
    if len(file) == 1:
        print("Error: Missing command-line argument.")
    else:
        try:
            read_file = open(f"{file_name}", "r")
            write_file(final_format(list_process(read_file.readlines())))
            read_file.close()
        except FileNotFoundError:
            print('Error: Cannot open "' + file_name + '". Sorry about that.')
