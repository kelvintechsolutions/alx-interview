#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    # Constants for UTF-8 byte patterns
    UTF8_BYTE_PATTERNS = {
        0b11110000: 4,  # 4-byte sequence
        0b11100000: 3,  # 3-byte sequence
        0b11000000: 2,  # 2-byte sequence
    }

    # State variable to track expected continuation bytes
    expected_continuation_bytes = 0

    for byte in data:
        # Validate byte type and range
        if not isinstance(byte, int) or not 0 <= byte <= 0x10ffff:
            return False

        # Mask the byte to determine its type
        masked_byte = byte & 0b11111000

        # Check if we're expecting continuation bytes
        if expected_continuation_bytes > 0:
            # Continuation byte expected, validate it
            if byte & 0b11000000!= 0b10000000:
                return False
            expected_continuation_bytes -= 1
        else:
            # Determine the byte sequence type
            if masked_byte in UTF8_BYTE_PATTERNS:
                # Multi-byte sequence, update expected continuation bytes
                expected_continuation_bytes = UTF8_BYTE_PATTERNS[masked_byte] - 1
                # Validate the sequence length
                if len(data) < len([byte]) + expected_continuation_bytes + 1:
                    return False
            elif masked_byte > 0b11110000 or byte & 0b10000000:
                # Invalid start byte
                return False
            # Single byte (ASCII) or valid start byte, no action needed
    # Ensure no continuation bytes are left unmatched
    return expected_continuation_bytes == 0
