"""
Generate a random project name.

Usage: python3 -m sksc.projectname
mhdc / methodical
mhdc / methodically
mhdc / methodological
"""

import random
import re


def generate() -> str:
    """ Generate a 4 letter code as project name. """
    return ''.join(random.choices('bcdfghjklmnpqrstvwxz', k=4))


def search(tmp: str) -> str:
    """ Create a REGEX from a 4 letter project code. """
    return f'^{tmp[0:1]}.*{tmp[1:2]}.*{tmp[2:3]}.*{tmp[3:4]}'


def names(tmp: str):
    """ Search for project names in the words file. """
    words = "/usr/share/dict/words"
    found = []

    with open(words, encoding='UTF-8') as word_file:
        lines = word_file.readlines()

        for line in lines:
            if re.findall(tmp, line):
                found.append(line.strip())

    return found


if __name__ == '__main__':
    FOUND = None

    while not FOUND:
        CODE = generate()
        REGEX = search(CODE)
        FOUND = names(REGEX)

    for name in FOUND:
        print(f'{CODE} / {name}')
