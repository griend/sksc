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
    seed = 'bcdfghjklmnpqrstvwxz'
    code = ''.join(random.choices(seed, k=4))
    return code


def search(code: str) -> str:
    tmp = f'^{code[0:1]}.*{code[1:2]}.*{code[2:3]}.*{code[3:4]}'
    return tmp


def names(search: str):
    words = "/usr/share/dict/words"
    found = list()

    with open(words) as f:
        lines = f.readlines()

        for line in lines:
            if re.findall(search, line):
                found.append(line.strip())

    return found


if __name__ == '__main__':
    code = None
    regex = None
    found = None

    while not found:
        code = generate()
        regex = search(code)
        found = names(regex)

    for name in found:
        print(f'{code} / {name}')
