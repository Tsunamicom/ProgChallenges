# Created in Python 3.4 by Kurtis Mackey

# Requirements:
# input of n computers (2 - 8) set by user
# for n computers, allow user to set locations for each computer
# calculate distances of all computer connections.
# find min distance required to connect all computers + 16*n feet extra
# display connections individually
# display total connection length

import math
import time
from itertools import combinations as comb
from itertools import permutations as perm
import random

locationsa = [(1, 1), (2, 2), (3, 3)]
locations = [(5, 19), (55, 28), (38, 101), (28, 62), (111, 84), (43, 116)]


def con_length(con_set):
    """Given a set of two coordinates, determine the distance between them"""
    return math.sqrt((con_set[0][0]-con_set[1][0])**2 + (con_set[0][1]-con_set[1][1])**2)

master = dict()
best = dict()
def combo_distances():
    best_dist = 9999999999999
    all_paths = perm(locations)
    for ii in all_paths:
        if ii in master:
            distance = master[ii]
        else:
            distance = 0
            step = 0
            for i in comb(ii, 2):
                if not step+1 >= len(ii):
                    i_set = (ii[step], ii[step+1])
                    if i_set in master:
                        i_setdist = master[i_set]
                    else:
                        i_setdist = con_length(i_set)
                        master[i_set] = i_setdist
                        master[i_set[::-1]] = i_setdist
                    step += 1
                    distance += i_setdist
            master[distance] = ii
            master[ii] = distance
            master[ii[::-1]] = distance
        if best_dist >= distance:
            best_dist = distance
    print(best_dist, master[best_dist])


combo_distances()

