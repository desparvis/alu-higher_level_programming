#!/usr/bin/python3
def islower(c):
    if len(c) != 1:
        raise ValueError("Input must be a single character.")
    return ord('a') <= ord(c) <= ord('z')
def main():
    cases = ['a', 'H', 'A', '3', 'g']
    for c in cases:
        strings = "lower" if islower(c) else "upper"
        print("{} is {}".format(c, strings))
if __name__ == main:
    main()
~            
