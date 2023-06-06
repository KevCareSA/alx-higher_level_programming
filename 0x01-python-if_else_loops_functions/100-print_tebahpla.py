#!/usr/bin/python3

ascii = 122
while ascii >= 97:
    reverse_ascii = ascii
    if reverse_ascii % 2 == 1:
        reverse_ascii -= 32
    print("{:c}".format(reverse_ascii), end="")
    ascii -= 1
