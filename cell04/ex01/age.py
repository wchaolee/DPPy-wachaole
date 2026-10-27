#!/usr/bin/env python3

age = int(input("Please tell me your age: "))

print(f"You are currently {age} years old.")

for year in [10, 20, 30]:
    print(f"In {year} years, you'll be {age + year} years old.")