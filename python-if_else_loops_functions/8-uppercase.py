#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if ord(char) >= 97 and ord(char) <= 122:
        uppercaseu = chr(ord(char) - 32)
        result += uppercaseu
        else:
        result += char
    print("{}".format(result))
if __name__ == "__main":
    uppercase("best")
    uppercase("Best School 98 Battery street")
