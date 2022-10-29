#!/usr/bin/env python3
import calendar
import statistics
if __name__ == '__main__':
    rainfall = ['max_month','min_month']
    for month in (calendar.month_name[1:]):
        user_input = (input(f"Enter rainfall for {month}: "))
        user_input = int(user_input[:-2])
        if all(i <= user_input for i in rainfall[2:]):
            rainfall[0] = month
        if all(i >= user_input for i in rainfall[2:]):
            rainfall[1] = month
        rainfall.append(user_input)
    print(f"\nMax Rainfall: {max(rainfall[2:])}mm in {rainfall[0]}")
    print(f"Min Rainfall: {min(rainfall[2:])}mm in {rainfall[1]}\n")
    print(f"Average: {statistics.mean(rainfall[2:]):.2f}mm.")
    print(f"Standard Deviation: {statistics.stdev(rainfall[2:]):.2f}mm.")
