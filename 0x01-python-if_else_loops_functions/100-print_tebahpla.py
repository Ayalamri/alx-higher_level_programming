#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -2):
    print(f"{chr(i)}{chr(i - 33)}", end='')
