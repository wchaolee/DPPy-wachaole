#!/usr/bin/env python3

import sys

params = sys.argv[1:]

if len(params) > 0:
    word_output = False
    for param in params:
        if not param.endswith("ism"):
            print(param + "ism")
            word_output = True

else:
    print("none")