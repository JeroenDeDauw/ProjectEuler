
'''
Created on August 23, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=14
'''

from timeit import Timer

NUMBER_RANGE = xrange( 1, 10 ** 6 )

sequenceLenghts = {1:1}

def collatz( n ):
    return n / 2 if n % 2 == 0 else n * 3 + 1

def getCollatzSequenceLength( n ):
    if ( not n in sequenceLenghts ):
        sequenceLenghts[n] = 1 + getCollatzSequenceLength( collatz( n ) )

    return sequenceLenghts[n]

def euler14():
    [getCollatzSequenceLength( n ) for n in NUMBER_RANGE]
    print reduce( lambda x, y: x if x[1] > y[1] else y, sequenceLenghts.items(), ( 1, 1 ) )

def main():
    t = Timer( 'euler14()', "from __main__ import euler14" )

    try:
        print t.timeit( 1 )
    except:
        print t.print_exc()

if __name__ == '__main__':
    main()
