#!/usr/bin/python2.7

'''
Created on June 10, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=5
'''

import math

def findLowestDivisableNumber( divisors ):
    if len( divisors ) == 0: return 0
    if len( divisors ) == 1: return divisors[0]

    number = divisors[-1] * divisors[-2]
    while True:


def euler5():
    findLowestDivisableNumber( range( 1, 20 ) )

def main():
    print euler5()

if __name__ == '__main__':
    main()
