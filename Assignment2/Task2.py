#!/usr/bin/env python3

from statistics import mean as avg

if __name__ == "__main__":
    list1, list2 = [], []
    print("Template file" + "\nPark Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!\n")
    while 1:
        data = input("> ")
        if data == "END" and len(list2) == 0:
            print("No data found. Nothing to do. What a pity.")
            break
        elif data == "END":
            print("\nTotal runners:", len(list1))
            print("Average Time: ", int(avg(list2)//60), f"minute{'' if int(avg(list2)//60) == 1 else 's'},",
                  int(avg(list2) % 60), f"second{'' if int(avg(list2) % 60) == 1 else 's'}")
            print("Fastest Time: ", min(list2)//60, f"minute{'' if min(list2)//60 == 1 else 's'},",
                  min(list2) % 60, f"second{'' if min(list2) % 60 == 1 else 's'}")
            print("Slowest Time: ", max(list2)//60, f"minute{'' if max(list2)//60 == 1 else 's'},",
                  max(list2) % 60, f"second{'' if max(list2) % 60 == 1 else 's'}")
            print("Best Time Here: Runner #", list1[list2.index(min(list2))], sep='')
            break
        else:
            if data.find("::") < 1 or not data[data.find("::") + 2:].isdigit():
                print("Error in data stream. Ignoring. Carry on.")
            else:
                list1.append(int(data[:data.find("::")]))
                list2.append(int(data[data.find("::") + 2:]))
