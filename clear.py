#!/usr/bin/env python

'''
Clears the directory.
'''

import os

TO_REMOVE = [
    '.aux',
    '.fdb_latexmk',
    '.log',
    '.out',
    '.gz',
    '.toc',
    '.bbl',
    '.blg',
    '.bcf',
    '.xml',
]


def main():

    for f in os.listdir('.'):
        extention = os.path.splitext(f)[1]
        if extention in TO_REMOVE:
            os.remove(f)


if __name__ == '__main__':
    main()
