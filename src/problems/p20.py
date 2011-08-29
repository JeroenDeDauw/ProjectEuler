
'''
Created on August 29, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=20
'''

from timeit import Timer

FACTORIAL = 100

def euler20():
    print sum( map( int, str( reduce( lambda x, y: x * y, xrange( 1, FACTORIAL ), 1 ) ) ) )

def main():
    t = Timer( 'euler20()', "from __main__ import euler20" )

    try:
        print t.timeit( 1 )
    except:
        print t.print_exc()

if __name__ == '__main__':
    main()
