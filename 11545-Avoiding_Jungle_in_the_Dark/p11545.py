# Done in Python 3.4 by Kurtis Mackey
# http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=694&page=show_problem&problem=2540

# Known:
# 1)  Need to calculate total hours of journey (if possible)
# 2)  Two biomes (Plains, Jungle)
# 3)  No Travel in or staying inside Jungle at Night
# 4)  Max Travel Time before rest is 16 hours.
# 5)  Rest is exactly 8 hours
# 6)  Can rest immediately after resting
# 7)  Journey Start at 6
# 8)  Day time = 6 to 17 (military)
# 9)  Night time = 18 to 24, 0 to 5 (miltary)
# 10) Takes 1 hour to travel between biomes



# Define Start Time and Current Time
start_time = 6
current_time = start_time


# Define Day and Night Cycles
day = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
night = [18, 19, 20, 21, 22, 23, 24, 1, 2, 3, 4, 5]


biomes = {'S': 'Start', '.': 'Plains', '*': 'Jungle', 'D': 'Finish'}
journey = ['S...****................***.D', 'S.......D']
max_leg = len(journey)


day_night = 'Day'


class Pilgrim():
    """ Define the Pilgrim and it's abilities/restrictions """
    def __init__(self, name='Pilgrim'):
        self.leg = 0
        self.name = name
        self.location = biomes[journey[self.leg][0]]
        self.rest = 8
        self.max_move = 16
        self.moves = self.max_move


    def travel(self, hours=1):
        if self.moves - hours >=  0:
            self.moves -= hours
        else:
            print('Unable to move, need to rest')
            return False

    def resting(self):
        print('Resting')
        self.moves = self.max_move


def time(time=current_time):
    if time > 24:
        time -= 24
    return time


def ptravel(player, hours=1):
    return player.travel(hours)






# Define Player
pilgrim = Pilgrim()

# Simple testing
print(pilgrim.location)
ptravel(pilgrim, 4)
print(pilgrim.moves)
ptravel(pilgrim, 12)
print(pilgrim.moves)
ptravel(pilgrim, 1)
pilgrim.resting()
print(pilgrim.moves)
ptravel(pilgrim)
print(pilgrim.moves)
