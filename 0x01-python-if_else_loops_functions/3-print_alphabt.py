#!/usr/bin/python3
for characters in range(97, 123):
    if chr(characters) is not 'q' and chr(characters) is not 'e':
        print("{}".format(chr(characters)), end="")
