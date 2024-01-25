#!/usr/bin/python3
import sys

file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines_processed = 0

def print_stats():
    """Print statistics"""
    print(f'Total file size: {file_size}')
    for key in sorted(status_codes.keys()):
        if status_codes[key]:
            print(f'{key}: {status_codes[key]}')

try:
    for line in sys.stdin:
        try:
            # Extract information from the line
            parts = line.split(' ')
            ip_address = parts[0]
            status_code = int(parts[-2])
            size = int(parts[-1])

            # Check if the line matches the expected format
            if parts[2] != 'GET' or parts[3] != '/projects/260' or parts[4] != 'HTTP/1.1"':
                continue

            # Update metrics
            file_size += size
            status_codes[status_code] += 1
            lines_processed += 1

            # Print statistics after every 10 lines
            if lines_processed % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            # Skip lines that do not match the expected format
            continue

except KeyboardInterrupt:
    # Print statistics if interrupted
    print_stats()
    sys.exit(0)

# Print final statistics
print_stats()
