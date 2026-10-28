#!/usr/bin/env python3

import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    while len(text) < 8:
        text += 'Z'
    print(text)

params = sys.argv[1:]

if len(params) > 0:
    for param in params:
        lenght = len(param)
        if lenght > 8:
            shrink(param)
        elif lenght < 8:
            enlarge(param)
        else:
            print(param)
else:
    print("none")