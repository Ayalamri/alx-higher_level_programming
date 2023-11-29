#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -2):
    print("{}".format(chr(i)), end='')
    print("{}".format(chr(i - 33)), end='')
