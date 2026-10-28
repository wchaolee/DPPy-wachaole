#!/usr/bin/env python3

def greetings(name="noble strager"):
    if isinstance(name, str):
        print(f"Hello, {name}")
    else:
        print("Error! It was not a name.")

greetings("Wasana")
greetings("Roatmey")
greetings()
greetings(27)
