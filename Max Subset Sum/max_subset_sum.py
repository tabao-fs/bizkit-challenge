#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    a = 0
    b = 0

    for value in arr:
        if a > b:
            tmp = a
        else:
            tmp = b
        b = a + value
        a = tmp

    if a > b:
        return a
    else:
        return b


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    print(maxSubsetSum(arr))
