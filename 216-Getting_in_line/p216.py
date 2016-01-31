# Created in Python 3.4 by Kurtis Mackey

# Requirements:
# input of n computers (2 - 8) set by user
# for n computers, allow user to set locations for each computer
# calculate distances of computer 1 to each computer, find smallest.  Do for all computers.
# find min distance required to connect all computers + 16*n feet extra
# display connections individually
# display total connection length

import math


def conn_length(loc1, loc2):
    return math.sqrt((loc2[0]-loc1[0])**2 + (loc2[1]-loc1[1])**2)


"""
test_locations = {1: (1, 1), 2: (2, 2)}
print(test_locations[1])

print(conn_length(test_locations[1], test_locations[2]))

# print('%.2f' % conn_length((1, 1), (2, 2))) #= 1.41  (print shows round to 2 decimal values)
"""  #Test of conn_length

