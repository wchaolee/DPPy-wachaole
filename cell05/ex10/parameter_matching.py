#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    target = sys.argv[1]

    word_output = input("What was the parameter? ")

    if word_output == target.lower():
        print("Good job!")
    else:
        print("Nope sorry...")
else:
    print("none")