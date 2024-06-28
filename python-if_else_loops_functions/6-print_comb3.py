#!/usr/bin/python3
for l in range(10):
    for k in range(l + 1, 10):
        if l != k:
            if l == 0 and k == 1:
                print("{:02}".format(l * 10 + k), end="")
            else:
                print(", {:02}".format(l * 10 + k), end="")
