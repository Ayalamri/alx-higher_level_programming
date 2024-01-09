#!/usr/bin/python3
'''Script for computing metrics from stdin.'''

import sys

def print_stats(total_size, status_codes):
    '''Prints statistics.'''
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def main():
    '''Main function to compute and print statistics.'''
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    count = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                total_size += int(parts[-1])
                status_code = parts[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except Exception:
                pass

            count += 1
            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
