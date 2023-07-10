#!/usr/bin/python3
"""a class MyInt that inherits from int."""


class MyInt(int):
    """Inverts int operators == and !=."""

    def __eq__(self, value):
        """Override opeartors"""
        return self.real != value

    def __ne__(self, value):
        """Override operators"""
        return self.real == value
