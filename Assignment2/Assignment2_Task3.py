#!/usr/bin/env python3

import process

if __name__ == "__main__":
    my_file = open("students.txt", "r")
    data = my_file.read()  # data is a type str
    data_into_list = data.split("\n")  # data_into_list is a type list
    my_file.close()
    my_list = process.list_process(data_into_list)  # print(my_list[0][:]) print(my_list[1][:]) print(my_list[2][:])
    final_list = []
    for n in range(0, len(my_list[0][:])):
        final_list.append(my_list[0][n] + " " + my_list[1][n] + "@poppleton.ac.uk")
    print(final_list)
