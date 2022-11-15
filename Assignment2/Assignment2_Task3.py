#!/usr/bin/env python3

import process

if __name__ == "__main__":
    with open("students.txt", "r") as my_file:
        data_into_list = my_file.readlines()
    my_list = process.list_process(data_into_list)  # print(my_list[0][:]) print(my_list[1][:]) print(my_list[2][:])
    final_list = []
    for n in range(0, len(my_list[0][:])):
        final_list.append(my_list[0][n] + " " + my_list[2][n] + my_list[1][n] + "@poppleton.ac.uk")
    print(final_list)
