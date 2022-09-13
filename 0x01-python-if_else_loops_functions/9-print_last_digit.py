#!/usr/bin/python3

# 9-print-last_digit
def print_last_digit(number):
    """Prints the last digit of a number"""
    if number > 0:
        print("{:d}".format(-(number % -10, end="")))
        return(-(number % -10)
    else:
        print("{:d}".format(number % 10)
        return(number % 10)
