#!/usr/bin/python3

"""
Method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Checks if the given byte sequence represents a valid UTF-8 encoding.
    Note: Each integer represents 1 byte of data, therefore you only
    need to handle the 8 least significant bits of each integer

    Args:
        data: A list of integers representing bytes.

    Returns:
        True if the data is a valid UTF-8 encoding, False otherwise.
    """

    for num in data:
        bin_rep = format(num, '08b')
        if bin_rep.startswith('0') or\
                bin_rep.startswith('110') or\
                bin_rep.startswith('1110') or\
                bin_rep.startswith('11110'):
            continue
        else:
            return False
    return True
