Avoiding Jungle in the Dark Problem:
Taken from http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=694&page=show_problem&problem=2540

A Pilgrim is all set for a long journey to the Holy land. The journey is long and involves covering
dangerous grounds. In particular, he needs to go through two types of land, plain and jungles. It is
safe to be located on a plain ground during any hour of the day, but traveling into or staying in the
jungle must be avoided during dark hours. Also, the Pilgrim is a human so he must take rests. He can
not travel continuously for more than 16 hours; he will need a rest after that. However, he can decide
to have a rest anytime he wants, even after getting up from one rest session. Once he decides to take
a rest, he must do so for exactly 8 hours.

Given the map of the route, help the Pilgrim to determine the minimum time that would be required
to travel from the starting position to the destination.


Input

The first line of input contains a positive integer T ≤ 100. Each of the next T lines contains a string
of length at least 2 and at most 1000. The string will always begin with an S and end with a D. The
characters in between will be either a ‘.’ or ‘*’, quotes for clarity. Here a ‘.’ represents a plain land
and ‘*’ a jungle. It takes exactly one hour to travel from one position to the next and the Pilgrim
never travels backward. Note that he is always located at the left most position of a particular land
and when he travels to the next land, he travels for a full hour to the reach the left most position of
the next land.


Output

For each case of input there will be one line of output. It will first contain the case number followed by
the minimum time required to reach the destination. In case it is not possible to reach the destination,
output ‘-1’. Note that he starts his journey from the position marked S and finishes at D. On the first
day of his journey, he is located on S at 6 AM. Dark hours are considered to be the time between 6
PM to 6 AM inclusive.


Sample Input

3

S.......D

S...****................***.D

S***********.***********D


Sample Output

Case #1: 8

Case #2: 36

Case #3: -1

