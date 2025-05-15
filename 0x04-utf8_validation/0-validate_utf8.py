#!/usr/bin/python3
"""UTF-8 validation module.
"""

def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    num_bytes_remaining = 0

    for byte in data:
        byte = byte & 0xFF  # Only consider the least significant 8 bits

        if num_bytes_remaining == 0:
            # Determine how many bytes the UTF-8 character needs
            if (byte >> 7) == 0:
                # 1-byte character (0xxxxxxx)
                continue
            elif (byte >> 5) == 0b110:
                num_bytes_remaining = 1
            elif (byte >> 4) == 0b1110:
                num_bytes_remaining = 2
            elif (byte >> 3) == 0b11110:
                num_bytes_remaining = 3
            else:
                # Invalid starting byte
                return False
        else:
            # Must be a continuation byte (starts with 10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            num_bytes_remaining -= 1

    # All characters should have completed properly
    return num_bytes_remaining == 0

