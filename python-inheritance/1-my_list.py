#!/usr/bin/python3
"""define list"""


class MyList(list):
    """list class"""
    def print_sorted(self):
        """sorted list"""
        print(sorted(self))
