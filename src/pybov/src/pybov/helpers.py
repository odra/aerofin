"""
This module contains useful functions that don't fit anywhere.
"""


def fill_str(s: str, full_size: int, char: str = ' ', order: int = 1) -> str:
    """
    Fills a string with extra characters based on full_size.

    This is used so data classes can convert themselves to the original
    string value they parsed from.
    """
    spaces = full_size - len(s)

    if spaces <= 0:
        return s

    filled = [char for c in range(0, spaces)]

    if order == 1:
        return ''.join([s] + filled)

    return ''.join(filled + [s])


def str2int(s: str) -> int:
    """
    Converts a string into an int.

    The new int value is returned leaving the original
    string untouched.
    """
    data = s.strip()

    if not data:
        return 0

    return int(s)


def write_file(path: str, contents: str) -> None:
    """
    Write contents to a file (path) using mode 'w+'.
    """
    with open(path, 'w+') as f:
        f.write(contents)
