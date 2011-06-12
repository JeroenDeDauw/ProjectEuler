#!/usr/bin/python2.7

'''
Created on June 10, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=4
Second version
'''

import math, random
from timeit import Timer

def isPalindromic1( string ):
#    if string == "":
#        string = "".join( random.choice( "0123456789" ) for x in range( 6 ) )

    l = len( string )
    return string[:l / 2] == string[:l - ( l / 2 ) - 1:-1]

def isPalindromic2( string ):
#    if string == "":
#        string = "".join( random.choice( "0123456789" ) for x in range( 6 ) )

    return string == string[::-1]

def findHighestPalindromic( firstRange, secondRange ):
    highestPalindromic = 0
    first = firstRange[1]

    while first >= firstRange[0]:
        second = secondRange[1]

        while second >= secondRange[0]:
            product = first * second
            p = str( product )

            if p == p[::-1] and product > highestPalindromic:
                highestPalindromic = product

            second -= 1
        first -= 1

    return highestPalindromic

def euler4( productSize ):
    range = ( int( math.pow( 10, productSize - 1 ) ), int( math.pow( 10, productSize ) - 1 ) )
    return findHighestPalindromic( range, range )

def main():
    print euler4( 3 )

#    t1 = Timer( 'isPalindromic1( "123456977654321" )', "from __main__ import isPalindromic1" )
#    t2 = Timer( 'isPalindromic2( "123456977654321" )', "from __main__ import isPalindromic2" )
#
#    try:
#        print t2.timeit( 900100 )
#    except:
#        print t2.print_exc()
#
#    try:
#        print t1.timeit( 900100 )
#    except:
#        print t1.print_exc()

if __name__ == '__main__':
    main()
