#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("0 arguments")
    else :
        print("{} argument:".format(argc))
        for i in range(argc):
            print("{}: {}".format(i + 1, argv[i]))

if __name__ == "__main__":
    main()
