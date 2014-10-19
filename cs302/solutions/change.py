# change.py for Assignment 4 in CS 302

__author__ = "Paul Bae"

def max_coins(cents, value, singular, plural):
    """
    This function, given the cents and value of the coin as parameters
    Outputs the maximum number of coin(s) that can fit into cents pluralized
    """
    
    coins = cents / value
    if coins == 1:
        print coins, singular, "  ",
    elif coins > 1:
        print coins, plural, "  ",

    return coins
    

def make_change(cents):
    """docstring for make_change"""
    if not 0 < cents < 100:
        return

    print "The change for", cents, "cents is:"

    quarters = max_coins(cents, 25, "quarter", "quarters")
    cents -= quarters * 25

    dimes = max_coins(cents, 10, "dime", "dimes")
    cents -= dimes * 10
    
    nickels = max_coins(cents, 5, "nickel", "nickels")
    cents -= nickels * 5

    max_coins(cents, 1, "penny", "pennies");

cents = input("Enter a whole number of cents (from 1 to 99). I will output the number of coins that equals that amount: ");

make_change(cents)
