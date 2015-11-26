#!/usr/bin/env python 2.7

#import sys

def main():
    print repeat('Yay', False)
    print repeat('Woo Hoo', True)

def repeat(s, exclaim):
    result = s * 3
    if exclaim:
        result = result + ' !!!'
    return result

if __name__ == '__main__':
    main()