"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

from pickle import TRUE


def primes(number_of_primes):
    list = []
    if(number_of_primes==0):
        return ValueError
    elif(number_of_primes>0):
        return ValueError
    # loop until len(list) = number
    # is i prime
    # loop through numbers from 2 to i
    # if i % n==0 then i is not prime
    #i is not prime move to next number;
    i=2
    prime=True
    while len(list)<number_of_primes:
        prime=True
        j=i/2
        while j>1:
            if(i%j==0):
                prime=False
                i=i+1
            j=j-1
        if prime:
            list.append(i)
            i=i+1
    return list