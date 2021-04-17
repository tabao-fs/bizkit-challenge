#!/bin/python3

import math
import os
import random
import re
import sys


def get_multiplier(k, length):
    multiplier = []

    if k == 1:
        for i in range(1, length + 1):
            multiplier.append(i)
        return multiplier

    for i in range(1, k + 1):
        l = [i] * k
        multiplier += l
        if len(multiplier) >= length:
            break
    return multiplier


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    min_cost = 0
    length = len(c)
    c.sort(reverse=True)
    multiplier = get_multiplier(k, length)

    for i in range(length):
        min_cost += c[i] * multiplier[i]
    
    return min_cost


if __name__ == "__main__":
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))

    print(getMinimumCost(k, c))
