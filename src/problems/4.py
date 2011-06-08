#!/usr/bin/python2.7

'''
Created on June 9, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=4
'''

import math

def findHighestPalindromic( firstRange, secondRange ):
    highestPalindromic = 0
    first = firstRange[1]

    while first >= firstRange[0]:
        second = secondRange[1]

        while second >= secondRange[0]:
            product = first * second
            p = str( product )
            l = len( p )
            if p[:l / 2] == p[:l - ( l / 2 ) - 1:-1] and product > highestPalindromic:
                highestPalindromic = product

            second -= 1
        first -= 1

    return highestPalindromic

def euler4( productSize ):
    range = ( int( math.pow( 10, productSize - 1 ) ), int( math.pow( 10, productSize ) - 1 ) )
    return findHighestPalindromic( range, range )

def main():
    print euler4( 3 )

if __name__ == '__main__':
    main()
