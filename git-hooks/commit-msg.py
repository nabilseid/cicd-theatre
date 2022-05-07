#!/usr/bin/python 

import sys

def main():
    with open(sys.argv[1]) as fp:
        lines = fp.readlines()
        print(lines)

    sys.exit(0)

if __name__ == '__main__':
    main()
