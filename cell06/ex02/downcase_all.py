#!/usr/bin/env python3

import sys

def downcase_it(text):
    return text.lower()

params = sys.argv[1:]

if len(params) > 0:
    for param in params:
        print(downcase_it(param))
else:
    print("none")

