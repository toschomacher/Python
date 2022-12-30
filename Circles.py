#!/usr/bin/env python3

if __name__ == "__main__":
    from math import pi
    counter = 1
    num_of_circles = int(input("Enter number of circles: "))
    result = []
    for n in range(num_of_circles):
        print("Enter r" + str(counter), " value: ", end="")
        counter += 1
        r1 = float(input(""))
        result.append(r1)
        print("Enter r" + str(counter), " value: ", end="")
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
        print("Circle", x+1, " with R1=", result[x*5], " R2=", result[x*5+1], " avR=", result[x*5+2],
              " C=", result[x*5+3], " A=", result[x*5+4])
