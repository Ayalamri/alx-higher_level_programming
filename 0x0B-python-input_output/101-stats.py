#!/usr/bin/python3
"""
Script to compute metrics from stdin
"""

import signal
import sys

def print_metrics(total_size, status_counts):
    """
    Print metrics based on the total size and status counts.
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

def signal_handler(sig, frame):
    """
    Handle keyboard interruption (CTRL + C) to print metrics.
    """
    print_metrics(total_size, status_counts)
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Initialize variables to keep track of metrics
total_size = 0
status_counts = {}

try:
    # Read stdin line by line
    for i, line in enumerate(sys.stdin, 1):
        # Parse the line to extract status code and file size
        parts = line.split()
        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update metrics
        total_size += file_size
        status_counts[status_code] = status_counts.get(status_code, 0) + 1

        # Print metrics every 10 lines
        if i % 10 == 0:
            print_metrics(total_size, status_counts)

except KeyboardInterrupt:
    # Handle keyboard interruption to print final metrics
    print_metrics(total_size, status_counts)
    sys.exit(0)
