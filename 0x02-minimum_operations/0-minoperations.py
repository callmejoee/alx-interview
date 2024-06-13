#!/usr/bin/python3
''' first problem '''


def minOperations(n):
    ''' function to solve the first module '''
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
