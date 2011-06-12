#!/usr/bin/python2.7

'''
Created on June 12, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=10
'''

from timeit import Timer
from p3 import getNextPrime

def sumOfPrimesInRange( lowerBound, upperBound ):
    '''
    Upper bound not included.
    '''
    sum = 0
    lowerBound = getNextPrime( lowerBound - 1 )

    while lowerBound < upperBound:
        #print sum, ' += ', lowerBound
        sum += lowerBound
        lowerBound = getNextPrime( lowerBound )

    return sum

def euler10():
    print sumOfPrimesInRange( 2, 2 * 10 ** 6 )

def main():
    t = Timer( 'euler10()', "from __main__ import euler10" )

    try:
        print t.timeit( 1 )
    except:
        print t.print_exc()

if __name__ == '__main__':
    main()
