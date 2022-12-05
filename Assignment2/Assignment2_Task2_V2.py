#!/usr/bin/env python3


def average(parameter):
    return parameter // 60


def remainder(parameter):
    return parameter % 60


def plural(parameter):
    return str(f"{'' if parameter == 1 else 's'}")


def data_output():
    avrg, minimum, maximum = int(avg(times)), min(times), max(times)
    print("\nTotal runners:", len(runners))
    print("Average Time: ", average(avrg), "minute" + plural(average(avrg)) + ",",
          remainder(avrg), "second" + plural(remainder(avrg)))
    print("Fastest Time: ", average(minimum), "minute" + plural(average(minimum)) + ",",
          remainder(minimum), "second" + plural(remainder(minimum)))
    print("Slowest Time: ", average(maximum), "minute" + plural(average(maximum)) + ",",
          remainder(maximum), "second" + plural(remainder(maximum)))
    print("Best Time Here: Runner #" + str(runners[times.index(minimum)]))


def data_alignment():
    runners.append(int(data[:data.find("::")]))
    times.append(int(data[data.find("::") + 2:]))


if __name__ == "__main__":
    from statistics import mean as avg
    runners, times = [], []
    print("Template file" + "\nPark Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!\n")
    while 1:
        data = input("> ")
        if data == "END" and len(times) == 0:
            print("No data found. Nothing to do. What a pity.")
            break
        elif data == "END":
            data_output()
            break
        else:
            if data.find("::") < 1 or not data[:data.find("::")].isdigit() or not data[data.find("::") + 2:].isdigit():
                print("Error in data stream. Ignoring. Carry on.")
            else:
                data_alignment()
