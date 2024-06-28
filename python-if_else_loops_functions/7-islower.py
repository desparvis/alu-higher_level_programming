#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord('c') <= ord('z')
def main():
    cases = ['a', 'H', 'A', '3', 'g']
    for c in cases:
        str = "lower" if slower(c) else "upper"
        print("{} is {}".format(c, str))
if __name__ == main:
    main()
~            
