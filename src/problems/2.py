#!/usr/bin/python2.7

'''
Created on Jun 8, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=2
'''

import math

def getFiboSum( upperLimit ):
    sum, prev, current = 0, 0, 1

    while current < upperLimit:
        if current % 2 == 0:
            sum += current
        prev, current = current, prev + current

    return sum

def main():
    print getFiboSum( 4 * math.pow( 10, 6 ) )

if __name__ == '__main__':
    main()
