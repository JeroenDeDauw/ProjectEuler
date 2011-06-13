#!/usr/bin/python2.7

'''
Created on June 13, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=11
'''

from timeit import Timer

def euler11():
    print ''

def main():
    t = Timer( 'euler11()', "from __main__ import euler11" )

    try:
        print t.timeit( 1 )
    except:
        print t.print_exc()

if __name__ == '__main__':
    main()
