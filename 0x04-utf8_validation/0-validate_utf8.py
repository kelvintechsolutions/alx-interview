#!/usr/bin/python3

def validUTF8(data):
    remaining_continuations = 0
    bytes_used = 0
    code_point = 0

    for num in data:
        byte = num & 0xFF

        if remaining_continuations == 0:
            # Start of a new character
            if (byte & 0x80) == 0x00:  # 1-byte character
                code_point = byte & 0x7F
                bytes_used = 1
                remaining_continuations = 0
            elif (byte & 0xE0) == 0xC0:  # 2-byte character
                code_point = byte & 0x1F
                bytes_used = 2
                remaining_continuations = 1
            elif (byte & 0xF0) == 0xE0:  # 3-byte character
                code_point = byte & 0x0F
                bytes_used = 3
                remaining_continuations = 2
            elif (byte & 0xF8) == 0xF0:  # 4-byte character
                code_point = byte & 0x07
                bytes_used = 4
                remaining_continuations = 3
            else:
                # Invalid start byte
                return False

            if bytes_used == 1:
                # 1-byte character is always valid
                pass
        else:
            # Processing continuation byte
            if (byte & 0xC0) != 0x80:
                return False
            code_point = (code_point << 6) | (byte & 0x3F)
            remaining_continuations -= 1

            if remaining_continuations == 0:
                # Check code point validity based on bytes_used
                if bytes_used == 2:
                    if not (0x80 <= code_point < 0x800):
                        return False
                elif bytes_used == 3:
                    if not (0x800 <= code_point < 0x10000):
                        return False
                    if 0xD800 <= code_point <= 0xDFFF:
                        return False
                elif bytes_used == 4:
                    if not (0x10000 <= code_point <= 0x10FFFF):
                        return False
                else:
                    return False  # This should not happen

    return remaining_continuations == 0
