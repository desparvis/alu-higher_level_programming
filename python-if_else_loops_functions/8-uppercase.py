#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if ord(char) >= 97 and ord(char) <= 122:
        uppercase = chr(ord(char) - 32)
        result += uppercase
    else:
        result += char
print(result)
