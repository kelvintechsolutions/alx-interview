#!/usr/bin/python3
"""UTF-8 validation module."""

def validUTF8(data):
    """Checks if a list of integers represents valid UTF-8 encoded data.
    
    Args:
        data: List of integers representing bytes (0-255)
        
    Returns:
        True if data is valid UTF-8, False otherwise
    """
    # Number of bytes remaining in the current UTF-8 character
    remaining_bytes = 0
    
    for byte in data:
        # Ensure each value is a valid byte (0-255)
        if not isinstance(byte, int) or byte < 0 or byte > 255:
            return False
        
        # Check if this is the start of a new character
        if remaining_bytes == 0:
            # 1-byte character (0xxxxxxx)
            if byte >> 7 == 0b0:
                remaining_bytes = 0
            # 2-byte character (110xxxxx)
            elif byte >> 5 == 0b110:
                remaining_bytes = 1
            # 3-byte character (1110xxxx)
            elif byte >> 4 == 0b1110:
                remaining_bytes = 2
            # 4-byte character (11110xxx)
            elif byte >> 3 == 0b11110:
                remaining_bytes = 3
            else:
                return False
        else:
            # Continuation bytes must be 10xxxxxx
            if byte >> 6 != 0b10:
                return False
            remaining_bytes -= 1
    
    # If we end in the middle of a character, it's invalid
    return remaining_bytes == 0
