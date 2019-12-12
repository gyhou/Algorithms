#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def bottom_up_cookie(n):
    """
    10 times faster than cache version
    """
    if n < 2:
        return 1
    elif n < 3:
        return 2
    prevprevprev = 0
    prevprev = 1
    prev = 1

    for _ in range(n-1):
        cur = prevprevprev + prevprev + prev
        prevprevprev = prevprev
        prevprev = prev
        prev = cur

    return cur


def eating_cookies(n):
    cache = {}

    def inner(n):
        if n < 2:
            return 1
        elif n < 3:
            return n
        elif n not in cache:
            cache[n] = inner(n-1) + inner(n-2) + inner(n-3)
        return cache[n]

    return inner(n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
