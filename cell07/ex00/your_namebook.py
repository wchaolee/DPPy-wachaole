#!/usr/bin/env python3

def array_of_names(persons_dict):
    result = []
    for first_name , last_name in persons_dict.items():
        fullname = f"{first_name.capitalize()} {last_name.capitalize()}"
        result.append(fullname)
    return result

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))