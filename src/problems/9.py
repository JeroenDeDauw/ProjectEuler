#!/usr/bin/python2.7

'''
Created on June 12, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=9
'''

from timeit import Timer

def findPythagoreanTriplet( sum ):
    for first, second in [( first, second ) for first in range( 1, sum + 1 ) for second in range( 1, sum + 1 )]:
        third = sum - first - second
        if first ** 2 + second ** 2 == third ** 2:
            return ( first, second, third )
    else:
        return False

def main():
    triplet = findPythagoreanTriplet( 1000 )

    if triplet:
        print triplet
        print reduce( lambda x, y: x * y, triplet )
    else:
        print 'Not found :('

    t = Timer( 'findPythagoreanTriplet( 1000 )', "from __main__ import findPythagoreanTriplet" )

    try:
        print t.timeit( 1 )
    except:
        print t.print_exc()

if __name__ == '__main__':
    main()
