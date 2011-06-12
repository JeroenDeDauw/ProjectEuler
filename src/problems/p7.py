#!/usr/bin/python2.7

'''
Created on June 10, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=7
'''
from Crypto.Util.number import isPrime

def findNthPrime( n ):
    currentCount = 1
    currentNumber = long( 2 )

    while currentCount < n:
        currentNumber += 1
        if isPrime( currentNumber ):
            currentCount += 1

    return currentNumber

def main():
    print findNthPrime( 6 )
    print findNthPrime( 10001 )

if __name__ == '__main__':
    main()
