#!/usr/bin/env python3

text = input("What you gotta say? : ").strip()

while True:
    if text == "STOP":
        break
    text = input("I got that! Anything else? : ")