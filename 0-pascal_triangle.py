#!/usr/bin/python3
def fact(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a


def combination(n, r):
    return fact(n) // (fact(n - r) * fact(r))


def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(combination(i, j))
        triangle.append(row)
    return triangle
