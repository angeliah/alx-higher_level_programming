#!/usr/bin/python3

# 5-print_comb2
"""prints numbers from 0 to 99,separated by coma,in two digits"""
for i in range(0, 100):
    if i == 99:
        print("{}".format(i))
    else:
        print("{:02}".format(i), end=",")
