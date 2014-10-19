# hailstone.py for Assignment 4 in CS 302

__author__ = "Paul Bae"

def solve(n):
    """
    The main evaluation loop
    """

    count = 0
    
    while n > 1:
        if n % 2:
            temp = 3*n+1
            print n, "is odd, so I take 3n + 1:", temp
            n = temp
        else:
            temp = n/2
            print n, "is even, so I take half", temp
            n = temp
        count += 1

    print "The process took", count, "steps to reach 1"

num = input("Enter a number: ")
solve(num)
