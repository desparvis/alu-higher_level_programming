#!/usr/bin/python3
"""
module define
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__
