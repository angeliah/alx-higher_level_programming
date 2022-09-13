#!/usr/bin/python3

# 5-print_comb2
"""prints numbers from 0 to 99,separated by coma,in two digits"""
for i in range(0, 99):
    print("{:02d}, ".format(i), end='')
print("{:02d}".format(i + 1))
