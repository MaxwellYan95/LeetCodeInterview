#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maximumRequests' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER window
#  2. INTEGER_ARRAY timestamps
#

def maximumRequests(window, timestamps):
    if len(timestamps) == 1:
        return 1;
    maxReq = 1;
    lowInd = 0;
    highInd = 1;
    while highInd < len(timestamps):
        while timestamps[highInd] - timestamps[lowInd] > window:
            lowInd += 1;
        maxReq = max(maxReq, highInd - lowInd + 1);
        highInd += 1;
    return maxReq

print(maximumRequests(4, [0, 0, 0, 0, 0, 0, 0, 0]))