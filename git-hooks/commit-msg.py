#!/usr/bin/python 

import sys

def main():
    print("Number of argument", len(sys.argv)) 
    print("Argument List", str(sys.argv))

    sys.exit(1)

if __name__ == '__main__':
    main()
