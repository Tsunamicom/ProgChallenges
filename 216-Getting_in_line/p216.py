# Created in Python 3.4 by Kurtis Mackey

# Requirements:
# input of n computers (2 - 8) set by user
# for n computers, allow user to set locations for each computer
# calculate distances of all computer connections.
# find min distance required to connect all computers + 16*n feet extra
# display connections individually
# display total connection length

import math


comp_loc = dict()
comp_loc['c1'] = (1, 4)
comp_loc['c2'] = (2, 5)
comp_loc['c3'] = (10, 10)
#comp_loc['c4'] = (5, 4)
#comp_loc['c5'] = (12, 15)
#comp_loc['c6'] = (1, 2)
#comp_loc['c7'] = (14, 30)
#comp_loc['c8'] = (16, 31)


def conn_length(loc1, loc2):
    """Given two sets of coordinates, determine the distance between them"""
    return math.sqrt((loc2[0]-loc1[0])**2 + (loc2[1]-loc1[1])**2)


def unique_combos():
    """
    Find unique connections given a dict of computers.
    Return a list of unique combinations.
    """

    # Find all possible combinations given a dict of computers
    complistz = list()
    for comp1 in comp_loc:
        for comp2 in comp_loc:
            complistz.append([comp1, comp2])


    # Find unique connections given the possible combinations
    unique_list = list()
    sortedlist = list()
    for i in complistz:
        for ii in complistz:
            if sorted(i) not in sortedlist:
                if i[0] != i[1]:
                    unique_list.append(sorted(i))
                    sortedlist.append(i)
                    sortedlist.append(sorted(i))

    return sorted(unique_list)


def con_w_dist():
    """
    Given unique connection, determine distance between those connections.
    Return a dictionary of (distance: connection)
    """

    connection_combos = unique_combos()
    connect_master = dict()
    for connection in connection_combos:
        con_dist = conn_length(comp_loc[connection[0]],
                               comp_loc[connection[1]])
        connect_master[con_dist] = sorted(connection)
    return connect_master


distances = con_w_dist()

dist_list = list()
print(distances)
sort_dist = sorted(distances.keys())
print('\n')
print(sort_dist)

for distance in sort_dist:
    print(distances[distance])



#  If [a1, a2], and [a1, a3], find shortest distance between the two.  return the shortest and
#  remove connection from list.  Take into account both that have been removed.
