#/usr/bin/env python3

import sys
arg_list = sys.argv[1:]
print(sorted(arg_list, key=len)[0])