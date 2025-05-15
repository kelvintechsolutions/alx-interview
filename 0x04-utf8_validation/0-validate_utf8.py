#!/usr/bin/python3
"""UTF-8 validation module.
"""

def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    num_bytes = 0

    for byte in data:
        byte = byte & 0xFF  # Consider only the least significant 8 bits

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                # If it starts with 1 but doesn't match any valid prefix
                return False
        else:
            # Check that the byte starts with '10'
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0

