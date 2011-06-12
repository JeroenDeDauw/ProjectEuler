#!/usr/bin/python2.7

'''
Created on June 10, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://projecteuler.net/index.php?section=problems&id=6
'''

def euler6( numbers ):
    return abs( sum( [ pow( nr, 2 ) for nr in numbers ] ) - pow( sum( numbers ), 2 ) ) 

def main():
    print euler6( range( 1, 10 + 1 ) )
    print euler6( range( 1, 100 + 1 ) )

if __name__ == '__main__':
    main()
