#!/usr/bin/env python3

# Name: Chelsea Parlett & Chris Watkins
# Student ID: 2298930 & 1450263
# Email: parlett@chapman.edu & watki115@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 4

def eratosthenes(n):
    potential_primes = list(i for i in range(2,n))
    for item in potential_primes:
        for item2 in potential_primes:
            if item != item2:
                if item2%item == 0:
                    potential_primes.remove(item2)
    return potential_primes

def main(argv):
    n = argv
    if n  <=0:
        print("You chose a negative number")
    else:
        return eratosthenes(n)
    

def gen_eratosthenes(n):
    i = 2
    while True:
        
    
if __name  == "__main__":
    import sys
    main(sys.argv[1])