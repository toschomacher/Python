#/usr/bin/env python3

from sys import platform
if platform == "linux" or platform == "linux2":
    print("OS: Linux")
elif platform == "darwin":
    print("OS: Mac OS X")
elif platform == "win32":
    print("OS: Windows")