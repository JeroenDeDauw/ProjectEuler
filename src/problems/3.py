#!/usr/bin/python2.7

'''
Created on Jun 8, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >
'''

def isPrime( number ):
    for divisor in range( 2, number ):
        if number % divisor == 0:
            False
    return True

def getNextPrime( lowerBound ):
    ''' Lower bound not included '''
    nextPrime = 0

    while nextPrime == 0:
        lowerBound += 1
        if isPrime( lowerBound ):
            nextPrime = lowerBound

    return nextPrime

def getPrimeFactors( number ):
    factors = []
    currentPrime = 1

    while number > 1:
        currentPrime = getNextPrime( currentPrime )
        primeIsDevisor = False

        while number % currentPrime == 0:
            number /= currentPrime
            primeIsDevisor = True

        if primeIsDevisor:
            factors.append( currentPrime )

    return factors

def main():
    print max( getPrimeFactors( 13195 ) )
    print max( getPrimeFactors( 600851475143 ) )

if __name__ == '__main__':
    main()
