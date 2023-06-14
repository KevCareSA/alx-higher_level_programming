#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_value = max(list(a_dictionary.values()))
    for key, val in a_dictionary.items():
        if val == max_value:
            return key
    return None
