#!/usr/bin/env python3

num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))
print("Thank you!")

for cal in ['+', '-', '/', '*']:
	result = eval(f"{num1} {cal} {num2}")
	print(f"{num1} {cal} {num2} = {result}")
