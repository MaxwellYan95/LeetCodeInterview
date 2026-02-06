#!/bin/python3
import heapq
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
    pow = 0;
    stack = []
    heapq.heapify(stack)
    xor = n;
    while 2**pow <= n:
        pow += 1;
    for num in range(n+1, 2**(pow)):
        p = pow;
        prevXor = xor;
        num2 = num;
        xor = 0;
        while prevXor > 0 or num2 > 0 or p >= 0:
            if 2**p <= num2 and 2**p <= prevXor:
                num2 -= (2**p)
                prevXor -= (2**p)
                p -= 1;
                continue;
            if 2**p <= num2:
                num2 -= (2**p)
                xor += (2**p)
            if 2**p <= prevXor:
                prevXor -= (2**p)
                xor += (2**p)
            p -= 1;
        heapq.heappush(stack, [xor, num])
    return heapq.heappop(stack)[1];

print(getMaxXor(12))

