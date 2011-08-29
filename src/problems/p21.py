
'''
Created on August 29, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=21
'''

from timeit import Timer

AMICABLE_RANGE_MIN = 0
AMICABLE_RANGE_MAX = 10 ** 4

def getProperDivisorsSum( n ):
    fn = float( n )
    divisors = set()
    
    for i in xrange( 1, int( n / 2 ) + 1 ):
        if ( fn / i ) % 2 == 0:
            divisors.add( i )
            divisors.add( fn / i )
    
    if n in divisors:
        divisors.remove( n )
        
    return sum( divisors )

def euler21():
    sums = [s for s in [( n, getProperDivisorsSum( n ) ) for n in xrange( AMICABLE_RANGE_MIN, AMICABLE_RANGE_MAX )] if s[1] <= AMICABLE_RANGE_MAX]
    amicableNrs = []
    
    for n, s in sums:
        if n == getProperDivisorsSum( s ):
            sums.remove( ( n, s ) )
            
            if n != s:
                amicableNrs.append( ( n, s ) )
                sums.remove( ( s, n ) )
    
    print amicableNrs
    print reduce( lambda x, y: x + y[0] + y[1], amicableNrs, 0 )

def main():
    t = Timer( 'euler21()', "from __main__ import euler21" )

    try:
        print t.timeit( 1 )
    except:
        print t.print_exc()

if __name__ == '__main__':
    main()
