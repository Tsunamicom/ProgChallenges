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

comp_loc = dict()
comp_loc['c1'] = (1, 4)
comp_loc['c2'] = (2, 5)
comp_loc['c3'] = (10, 10)
# comp_loc['c4'] = (5, 4)
# comp_loc['c5'] = (12, 15)
# comp_loc['c6'] = (1, 2)
# comp_loc['c7'] = (14, 30)
# comp_loc['c8'] = (16, 31)


def conn_length(loc1, loc2):
    """Given two sets of coordinates, determine the distance between them"""
    return math.sqrt((loc2[0]-loc1[0])**2 + (loc2[1]-loc1[1])**2)


def possible_combos():
    """
    Find unique cnnections given a dict of computers.
    Return a list of unique combinations
    """
    combinations = comb(comp_loc.keys(), 2)
    comblist = list()
    for i in combinations:
        comblist.append(list(sorted(i)))
    return comblist


def con_w_dist():
    """
    Given unique connection, determine distance between those connections.
    Return a dictionary of {Computer: {Connected Computer: Distance}}
    """
    connect_master = dict()
    connection_combos = possible_combos()
    for connection in connection_combos:

        # Calculate distances between all valid points
        con_dist = conn_length(comp_loc[connection[0]],
                               comp_loc[connection[1]])

        # Create a dictionary of all connections and distances
        if sorted(connection)[0] not in connect_master:
            connect_master[sorted(connection)[0]] = dict()
        connect_master[sorted(connection)[0]][sorted(connection)[1]] = con_dist

    return connect_master


distances = con_w_dist()

print(distances)


# Testing to find minimum and maximum distances
maxdist = 0
start = str
for con in distances:
    mindist = 999
    for con2 in distances[con]:
        l = distances[con][con2]
        if l >= maxdist:
            maxdist = l
        if l <= mindist:
            mindist = l
    print(str(mindist) + ' MIN')
print(str(maxdist) + ' MAX')

