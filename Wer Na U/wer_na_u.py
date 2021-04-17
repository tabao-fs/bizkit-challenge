#!/bin/python3

import math
import os
import random
import re
import sys


def compare(arr1, arr2, id=0):
    length = len(arr2)
    for i in range(id, len(arr1)):
        if length + i > len(arr1):
            return -1
        if arr1[i:length + i] == arr2:
            return i


# Complete the gridSearch function below.
def gridSearch(G, P):
    pid = 0
    prev_pid = 0
    p_length = len(P)
    got_str = "Got 'em"
    sorry_str = "Sorry Niko :("

    for arr in G:
        if pid == p_length:
            return got_str

        if prev_pid != 0:
            val = compare(arr, P[pid], prev_pid)
        else:
            val = compare(arr, P[pid])

        if val >= 0:
            if pid == 0:
                prev_pid = val
            if prev_pid != val:
                return sorry_str
            pid += 1

    return sorry_str


if __name__ == "__main__":
    t = int(input())

    for t_itr in range(t):
        RC = input().split()
        R = int(RC[0])
        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()
        r = int(rc[0])
        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        print(gridSearch(G, P))
