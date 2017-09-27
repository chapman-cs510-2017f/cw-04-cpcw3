#!/usr/bin/env python3

# Name: Chelsea Parlett & Chris Watkins
# Student ID: 2298930 & 1450263
# Email: parlett@chapman.edu & watki115@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 4

def eratosthenes(n):
    """ uses eratosthenes sieve to find primes"""
    potential_primes = list(i for i in range(2,n))
    for item in potential_primes:
        for item2 in potential_primes:
            if item != item2:
                if item2%item == 0:
                    potential_primes.remove(item2)
    return potential_primes

def era2(n):
    """ uses generator to find next prime"""
    p = []
    i = 2
    k = gen_eratosthenes()
    while i < n:
        i = next(k)
        p.append(i)
    return p   
# def main(argv):
#     n = int(argv)
#     if n  <=0:
#         print("You chose a negative number")
#     else:
#         return eratosthenes(n)
   

def gen_eratosthenes():
    """ uses while loop to define primes"""
    i = 2
    l_of_primes = []
    while True:
        a = list(i%x for x in l_of_primes)
        if 0 in a:
            i += 1
        else:
            l_of_primes.append(i)
            yield i
            i += 1

# f = gen_eratosthenes()
# print([next(f) for _ in range(9)])
# print(len([next(f) for _ in range(9)]))
       
   
if __name__  == "__main__":
   import sys
   main(sys.argv[1])
