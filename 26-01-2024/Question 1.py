"""Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

Input Format

A single integer denoting .

Constraints

Output Format

Print an integer denoting the best divisor of .

Sample Input 0

12
Sample Output 0

6
Explanation 0

The set of divisors of  can be expressed as . The divisor whose digits sum to the largest number is  (which, having only one digit, sums to itself). Thus, we print  as our answer.
"""
 

#!/bin/python3

import math

import os

import random

import re

import sys

def digit_sum(n):

    # Calculate the sum of digits of a number

    return sum(map(int, str(n)))
def find_best_divisor(n):

    best_divisor = 1

    max_digit_sum = 1
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            current_digit_sum = digit_sum(divisor)

            if current_digit_sum > max_digit_sum or (current_digit_sum == max_digit_sum and divisor < best_divisor):
                max_digit_sum = current_digit_sum
                best_divisor = divisor
    return best_divisor

def main():
    # Input the integer

    n = int(input())

    # Find and print the best divisor
    result = find_best_divisor(n)
    print( result)

if __name__ == "__main__":
    main()           
