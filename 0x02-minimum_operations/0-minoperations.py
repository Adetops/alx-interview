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


if __name__ == '__main__':
    minOperations = __import__('0-minoperations').minOperations

    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 2147483640
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
    # from random import randint
    # from time import time

    # start_time = time()

    # for i in range(10):
    #     n = randint(2, 100)
    #     print("Min # of operations to reach {} char: {}".
    #           format(n, minOperations(n)))

    # print(f'==> Program completed in {time() - start_time:.3f}s')
