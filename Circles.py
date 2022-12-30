#!/usr/bin/env python3

if __name__ == "__main__":
    from math import pi
    counter = 1
    num_of_circles = int(input("Enter number of circles: "))
    result = []
    r1 = 0.0
    r2 = 0.0
    for n in range(num_of_circles):
        if r1 == 0.0:
            print("Enter starting value for r" + str(counter), " value: ", end="")
            counter += 1
            r1 = float(input(""))
            result.append(r1)
        else:
            r1 = round((r2 + 0.2), 1)
            result.append(r1)
            print("Value for r" + str(counter), " = ", r1, "\n", end="")
            counter += 1
        if n == num_of_circles-1:
            print("Enter r" + str(counter), "value (final): ", end="")
        else:
            print("Enter r" + str(counter), "value: ", end="")
        counter += 1
        r2 = float(input(""))
        result.append(r2)
        r = (r1 + r2) / 4.0
        result.append(f"{r:.2f}")
        circumference = 2 * pi * r
        result.append(f"{circumference:.2f}")
        area = (r2 - r1) / 2 * circumference
        result.append(f"{area:.2f}")
    for x in range(num_of_circles):
        print("Circle ", x+1, " with Rin=", f"{result[x*5]:5.2f}", " Rout=", f"{result[x*5+1]:5.2f}",
              " Ravrg=", result[x*5+2], " Circ=", result[x*5+3], " Area=", result[x*5+4], "\n", end="")
