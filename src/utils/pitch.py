import re

lower = re.compile('[a-g]')
upper = re.compile('[A-G]')


def distance(a, b):
    """Returns the pitch distance between two notes
    Only used for chords for efficiency

Arguments:
a -- the first pitch to compare
b -- the second pitch to compare
"""
    a = a[0]
    b = b[0]
    if lower.search(a):
        if lower.search(b):
            return abs(ord(b) - ord(a)) % 8
        elif upper.search(b):
            return abs(ord(b.lower()) - ord(a)) % 5 + 8
    elif upper.search(a):
        if lower.search(b):
            return abs(ord(a.lower()) - ord(b)) % 5 + 8
        elif upper.search(b):
            return abs(ord(b) - ord(a)) % 8
    if a == b:
        return 0
    return 1
