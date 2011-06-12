#!/usr/bin/python2.7

'''
Created on June 10, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=5
'''

from sets import Set

def findLowestDivisableNumber( divisors ):
    '''
    Find the lowest number that can be wholy devided by all provided divisors. 
    '''
    divisors = getCleanedDivisors( divisors )
    
    if len( divisors ) == 0: return 0
    if len( divisors ) == 1: return divisors[0]

    number = divisors[-1] * divisors[-2]
    
    # Start with the first number divisable by the lowest divisor above the product of the two highest ones.
    if number % divisors[0] != 0:
        number = ( number / divisors[0] + 1 ) * divisors[0]
    
    while True:
        if isDibisibleNumber( number, divisors ):
            return number
        number += divisors[0]

def getCleanedDivisors( divisors ):
    '''
    Returns the cleaned version of a divisors list.
    Duplicates and insignificant divisors are removed, and the list is sorted ascending.
    '''
    divisors = sorted( list( Set( divisors ) ) )
    cleanedDivisors = []
    
    for divisor in divisors:
        if not hasHigherDivisor( divisor, divisors ):
            cleanedDivisors.append( divisor )
        
    return cleanedDivisors

def hasHigherDivisor( baseDivisor, divisors ):
    '''
    Returns if the divisors list contains a higher divisor that is a multiple of the
    provided devisor, thus rendering it insignificant. 
    '''
    for divisor in divisors:
        if divisor > baseDivisor and divisor % baseDivisor == 0:
            return True
    return False

def isDibisibleNumber( number, divisors ):
    '''
    returns if the number is devisable by all the provided divisors.
    '''
    for divisor in divisors:
        if number % divisor != 0:
            return False
    return True

def main():
    print findLowestDivisableNumber( range( 1, 10 ) )
    print findLowestDivisableNumber( range( 1, 20 ) )

if __name__ == '__main__':
    main()
