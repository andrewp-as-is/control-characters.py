__all__ = ['remove']


import unicodedata


def remove(string):
    """return a string without control characters"""
    return "".join(ch for ch in string if unicodedata.category(ch)[0] != "C")
