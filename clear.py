#!/usr/bin/env python

'''
Clears the directory according to '.gitignore'
'''

import os

TO_EXCEPT = [
    '.git',
    '.pdf',
]


def main():

    # read .gitignore
    with open('.gitignore') as f:
        lines = [l.strip('\n') for l in f.readlines()]

    # add files to except from .gitignore
    for line in lines:
        if len(line) > 0 and line[0] == '!':
            TO_EXCEPT.append(line.strip('!').strip('*'))

    # remove the files
    for file in os.listdir('.'):
        to_remove = True
        for e in TO_EXCEPT:
            if file.endswith(e):
                to_remove = False
                break

        if to_remove:
            os.remove(file)


if __name__ == '__main__':
    main()
