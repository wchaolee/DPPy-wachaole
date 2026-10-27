#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("none")
else:
    for param in sys.argv[1:][::-1]:
        print(param)