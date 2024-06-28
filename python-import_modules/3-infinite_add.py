#!/usr/bin/python3
import sys


def main():
    argv = sys.argv[1:]
    result = 0
    for arg in argv:
        result += int(arg)
    print(result)
if __name__ == "__main__":
    main()


