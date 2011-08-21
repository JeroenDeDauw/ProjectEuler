
'''
Created on August 22, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=12
'''

from timeit import Timer
from math import sqrt

MIN_DIVISORS = 501

def divisorGenerator( n ):
    for i in xrange( 1, int( sqrt( n ) ) + 1 ):
        if n % i == 0:
            yield i
            yield n / i;

def triangleGenerator():
    i = 0

    while True:
        i += 1
        yield sum( xrange( 1, i ) )

def euler12():
    triangles = triangleGenerator()
    divisors = set()

    while len( divisors ) < MIN_DIVISORS:
        triangleNumber = triangles.next()
        divisors = set( divisorGenerator( triangleNumber ) )

    print triangleNumber
    print len( divisors )
    print divisors

def main():
    t = Timer( 'euler12()', "from __main__ import euler12" )

    try:
        print t.timeit( 1 )
    except:
        print t.print_exc()

if __name__ == '__main__':
    main()
