#!/usr/bin/python3
# 3-print_alphabt.py

""" Print alphabet letters except q and e"""
for i in range (97, 123):
    if chr(i) is not 'e' and chr(i) is not 'q':
        print("{}".format(chr(i)), end="")
