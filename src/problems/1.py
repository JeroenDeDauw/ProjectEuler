'''
Created on Jun 8, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >
'''

import sys

def isMultiple( bases, number ):
    for base in bases:
        if number % base == 0:
            return True
    return False

def getMultiplesSum( bases, lowerLimit, upperLimit ):
    sum = 0
    for i in range( lowerLimit, upperLimit ):
        if isMultiple( bases, i ):
            sum += i
    return sum

def main():
    print getMultiplesSum( [3, 5], 0, 1000 )

if __name__ == '__main__':
    main()