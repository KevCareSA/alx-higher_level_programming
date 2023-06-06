#!/usr/bin/python3

for charact in range(ord('a'), ord('z') + 1):
    if chr(charact) != 'e' and chr(charact) != 'q':
        print('{:c}'.format(charact), end='')
