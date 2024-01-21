#!/usr/bin/python3


''' A module that returns the minimum Operations it takes to
    get to n characters.

    Available operations:
        copy all
        paste
'''


def minOperations(n):
    '''
    returns the minimum operations to get n H's
    '''
    min_operations = 0

    if n <= 1:
        return min_operations

    while n % 2 == 0:
        min_operations += 2
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            min_operations += i
            n //= i

    if n > 2:
        min_operations += n

    return min_operations
