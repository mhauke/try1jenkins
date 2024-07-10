#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2024 mh <mh@mhauke-lnx-jump>
#
# Distributed under terms of the MIT license.
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factorial.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("Number must be non-negative")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"The factorial of {number} is {factorial(number)}")
