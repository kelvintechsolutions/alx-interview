#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    if not data:
        return True

    i = 0
    while i < len(data):
        if data[i] <= 0x7F:
            # ASCII character (1 byte)
            i += 1
        elif data[i] <= 0xDF:
            # Invalid: should be 2-byte sequence but only 1 byte provided
            return False
        elif data[i] <= 0xE0:
            # 2-byte sequence
            if i + 1 >= len(data) or data[i + 1] < 0x80 or data[i + 1] > 0xBF:
                return False
            i += 2
        elif data[i] <= 0xEF:
            # 3-byte sequence
            if i + 2 >= len(data) or data[i + 1] < 0x80 or data[i + 1] > 0xBF or data[i + 2] < 0x80 or data[i + 2] > 0xBF:
                return False
            i += 3
        elif data[i] <= 0xF4:
            # 4-byte sequence
            if i + 3 >= len(data) or data[i + 1] < 0x80 or data[i + 1] > 0xBF or data[i + 2] < 0x80 or data[i + 2] > 0xBF or data[i + 3] < 0x80 or data[i + 3] > 0xBF:
                return False
            # Check if the codepoint is within the valid range for a 4-byte sequence
            codepoint = ((data[i] & 0x07) << 18) | ((data[i + 1] & 0x3F) << 12) | ((data[i + 2] & 0x3F) << 6) | (data[i + 3] & 0x3F)
            if codepoint > 0x10FFFF or (codepoint >= 0xD800 and codepoint <= 0xDFFF):
                return False
            i += 4
        else:
            # Invalid: should not be more than 4 bytes
            return False

    return True
