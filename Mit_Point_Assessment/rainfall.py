#!/usr/bin/env python3
import calendar
import statistics
from statistics import mean as avg
if __name__ == '__main__':
    rainfall = []
    max_month = "max"
    min_month = "min"
    for month in (calendar.month_name[1:]):
        user_input = (input(f"Enter rainfall for {month}: "))
        user_input = int(user_input[:-2])
        if all(i <= user_input for i in rainfall):
            max_month = month
        if all(i >= user_input for i in rainfall):
            min_month = month
        rainfall.append(user_input)

    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    avg_rainfall = avg(rainfall)

    print(f"\nMax Rainfall: {max_rainfall}mm in {max_month}")
    print(f"Min Rainfall: {min_rainfall}mm in {min_month}\n")
    print(f"Average: {avg_rainfall:.2f}mm.")
    print(f"Standard Deviation: {statistics.stdev(rainfall):.2f}mm.")
