#!/usr/bin/python3


rom_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }


def roman_to_int(roman_string):
    result = 0
    if not isinstance(roman_string, str):
        return result

    r_numeral = rom_num.keys()
    n = len(roman_string)
    i = 0
    while i < n:
        str_check1 = roman_string[i:i+2]
        str_check2 = roman_string[i]
        if str_check1 in r_numeral:
            result += rom_num.get(str_check1)
            i += 2
        elif str_check2 in r_numeral:
            result += rom_num.get(str_check2)
            i += 1

    return result
