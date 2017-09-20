#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Name: Chelsea Parlett & Chris Watkins
# Student ID: 2298930 & 1450263
# Email: parlett@chapman.edu & watki115@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 4
###

from primes import eratosthenes

def test_primes():
    #Tests eratosthenes for n = 23, 10, and 15
    assert eratosthenes(23) == [2,3,5,7,11,13,17,19]
    assert eratosthenes(10) == [2,3,5,7]
    assert eratosthenes(15) == [2,3,5,7,11,13]
    


