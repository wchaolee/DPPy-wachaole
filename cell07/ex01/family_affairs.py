#!/usr/bin/env python3

def find_the_redheads(family_duct):
    return list(filter(lambda name: family_duct[name] == "red", family_duct))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))