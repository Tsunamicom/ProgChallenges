# Created in Python 3.4 by Kurtis Mackey

# Requirements:
# input of n computers (2 - 8) set by user
# for n computers, allow user to set locations for each computer
# calculate distances of all computer connections.
# find min distance required to connect all computers + 16*n feet extra
# display connections individually
# display total connection length

from math import sqrt
import time
from itertools import combinations as comb
from itertools import permutations as perm




networks = [[(5, 19), (55, 28), (38, 101), (28, 62), (111, 84), (43, 116)], [(1, 1), (2, 2), (3,
                                                                                                3)]]


def con_length(con_set):
    """Given a set of two coordinates, determine the distance between them"""
    return sqrt((con_set[0][0]-con_set[1][0])**2 + (con_set[0][1]-con_set[1][1])**2)


def network_distances():
    """
    For each set of coordinates, calculate and store the distances between all coordinates.
    For variation ABC:  AB + BC:
        Find distances for AB, BC, and ABC
        Store these distances as well as the reversed (BA, CB, CBA) in master
        Also store the actual distance as a key in master
    Return the best path with the shortest distance
    Also store each set in a list for iteration
    """

    for locations in networks:
        best_dist = 999999999999
        best = list()
        for variation in perm(locations):
            if variation in master:
                distance = master[variation]    # Get distance from memo
            else:
                distance = 0
                step = 0
                for subvar in comb(variation, 2):
                    if not step+1 >= len(variation):
                        subvar_set = (variation[step], variation[step+1])
                        if subvar_set in master:
                            subvar_setdist = master[subvar_set]
                        else:
                            subvar_setdist = con_length(subvar_set)
                            master[subvar_set] = subvar_setdist        # Store for memo
                            master[subvar_set[::-1]] = subvar_setdist  # Store reverse for memo

                        step += 1
                        distance += subvar_setdist

                master[distance] = variation
                master[variation] = distance          # Store for memo
                master[variation[::-1]] = distance    # Store reverse for memo

            if best_dist >= distance:
                best_dist = distance


        # For each network, store the best connection sets in the network list for print iteration
        substep = 0
        for connections in master[best_dist]:

            if not substep+1 >= len(master[best_dist]):
                connection_step = (master[best_dist][substep], master[best_dist][substep+1])
                best.append([connection_step[0], connection_step[1], master[connection_step]])
                substep += 1

        network_list.append(best)

def printout(net_list):

    network_count = 1
    for networks in net_list:
        net_dist = 0
        print('********************************************************')
        print('Network %s' % network_count)
        for data in networks:
            print('Cable requirement to connect %s to %s is %.2f feet.' % (data[0], data[1], data[2]+16))
            net_dist += data[2]+16
        print('Number of feet of cable required is %.2f.' % net_dist)
        network_count += 1



if __name__ == '__main__':

    master = dict()
    network_list = list()

    network_distances()
    printout(network_list)

