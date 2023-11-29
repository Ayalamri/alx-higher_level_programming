#!/usr/bin/python3
for i in range(ord('Z'), ord('A') - 1, -1):
    print(f"{chr(i + 32)}{chr(i)}", end='')
