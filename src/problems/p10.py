#!/usr/bin/python2.7

'''
Created on June 12, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=10
'''

from timeit import Timer
from p3 import getNextPrime

#def prime_sieve(limit):
#        """Sieve of Atkin implmentation,
#        finds primes < limit.
#        It works by popping off prime numbers from the
#        head of a list, and removing all multiples of that prime.
#        
#        For optimization purposes, the sieve stops at sqrt(limit),
#        the remaining list is all primes.
#        """
#        pots = range(2, limit+1)
#        l = math.sqrt(limit)
#        p = 0
#        while p < l:
#                p = pots.pop(0)
#                yield p
#                pots = [i for i in pots if i%p != 0]
#        for i in pots:
#                yield i

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
