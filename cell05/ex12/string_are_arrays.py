#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    text = sys.argv[1]

    z_result = ""
    for char in text:
        if char == 'z':
            z_result += 'z'

    if len(z_result) > 0:
        print(z_result)
    else:
        print("none")
else:
    print("none")