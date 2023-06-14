#!/usr/bin/python3

# multiplies values my 2 and returns a new dict
def multiply_by_2(a_dictionary):
    new_diction = a_dictionary.copy()
    for key in new_diction.keys():
        new_diction[key] = new_diction[key] * 2

    return new_diction
