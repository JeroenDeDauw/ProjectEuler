
'''
Created on August 23, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=15
'''

from timeit import Timer

def euler15():
    print reduce( lambda i, j: i + int( j ), str( 2 ** 1000 ), 0 )

def main():
    t = Timer( 'euler15()', "from __main__ import euler15" )

    try:
        print t.timeit( 1 )
    except:
        print t.print_exc()

if __name__ == '__main__':
    main()
