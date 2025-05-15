#!/usr/bin/python3
"""UTF-8 validation module."""


def validUTF8(data):
    """Checks if a list of integers represents valid UTF-8 encoded data.
    
    Args:
        data: List of integers representing bytes (0-255)
        
    Returns:
        True if data is valid UTF-8, False otherwise
    """
    n = len(data)
    i = 0
    while i < n:
        # Validate current byte is within 0-255
        if not isinstance(data[i], int) or data[i] < 0 or data[i] > 255:
            return False
        
        byte = data[i]
        
        # Determine the number of bytes in the current UTF-8 character
        if byte < 0x80:
            # 1-byte character
            i += 1
            continue
        elif (byte & 0xE0) == 0xC0:
            # 2-byte character (must be >= 0xC2 to avoid overlong)
            if byte < 0xC2:
                return False
            num_bytes = 2
        elif (byte & 0xF0) == 0xE0:
            # 3-byte character
            num_bytes = 3
        elif (byte & 0xF8) == 0xF0:
            # 4-byte character (must be <= 0xF4 for valid Unicode)
            if byte > 0xF4:
                return False
            num_bytes = 4
        else:
            # Invalid leading byte
            return False
        
        # Check if there are enough bytes left
        if i + num_bytes > n:
            return False
        
        # Check continuation bytes
        for j in range(1, num_bytes):
            if (data[i + j] & 0xC0) != 0x80:
                return False
        
        # Calculate code point and validate ranges
        if num_bytes == 2:
            code_point = ((byte & 0x1F) << 6) | (data[i + 1] & 0x3F)
            if code_point < 0x80:
                return False
        elif num_bytes == 3:
            code_point = ((byte & 0x0F) << 12) | ((data[i + 1] & 0x3F) << 6) | (data[i + 2] & 0x3F)
            if code_point < 0x800:
                return False
            # Check for surrogates
            if 0xD800 <= code_point <= 0xDFFF:
                return False
            # Check for specific 3-byte constraints
            if byte == 0xE0 and (data[i + 1] & 0xFF) < 0xA0:
                return False
            if byte == 0xED and (data[i + 1] & 0xFF) > 0x9F:
                return False
        elif num_bytes == 4:
            code_point = ((byte & 0x07) << 18) | ((data[i + 1] & 0x3F) << 12) | ((data[i + 2] & 0x3F) << 6) | (data[i + 3] & 0x3F)
            if code_point < 0x10000 or code_point > 0x10FFFF:
                return False
            # Check specific 4-byte constraints
            if byte == 0xF0 and (data[i + 1] & 0xFF) < 0x90:
                return False
            if byte == 0xF4 and (data[i + 1] & 0xFF) > 0x8F:
                return False
        
        i += num_bytes
    
    return True
