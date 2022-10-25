#/usr/bin/env python3

import sys

count = len(sys.argv)-1

# Solution 1
print("\nSolutuin 1")
if count == 0:
    print("No arguments provided.")
elif count == 1:
    print(f"There is {count} argument provided.")
else:
    print(f"There are {count} number of arguments provided.")
    
# Solution 2
print("\nSolutuin 2")
# Notice how we use different quotes inside the print statement in order to work this way
print(f"There {'is' if count == 1 else 'are'} {count} argument{'' if count == 1 else 's'} provided.\n")