#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaxXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def getMaxXor(n):


def binary(n: int):
    pow = 0;
    curN = n;
    while 2**pow < n:
        pow += 1;
    result = ""
    while curN > 0:
        if 2**pow <= curN:
            result = "1" + str(result);
            curN -= 2**pow
        else:
            result = "0" + str(result);
            pow -= 1;
    if result[0] == '0':
        return result[1:]
    return result

def intToBinary(seq: str):
    pow = 0;
    result = 0;
    for s in seq[::-1]:
        if s == '1':
            result += (2**pow);
        pow += 1;
    return result


# Write your code here