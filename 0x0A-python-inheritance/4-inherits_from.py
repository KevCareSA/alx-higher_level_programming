#!/usr/bin/python3
"""An inherited class-checking function.
"""


def inherits_from(obj, a_class):
    """ Check for direct or indirect inheritance """
    if (type(obj) != a_class):
        return isinstance(obj, a_class)
    return False
