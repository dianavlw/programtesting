"""
HackerRank Interview Preparation Kit > Warm-up Challenges

SALES BY MATCH

There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example
n = 7
ar = [1,2,1,2,1,3,2]

There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

"""

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    count = 0
    d ={}
    
    for i in ar:
        d[i] = d.get(i, 0) + 1
    
    for i in d.keys():
        count += d[i]//2
    return count        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()



"""
COUNTING VALLEYS

An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Sample Input: 
8
UDDDUDUU
 
Sample Output:
1

"""

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    count = 0
    res = 0
    
    for c in path:
        if c == 'U':
            count += 1
        else: 
            count -=1
        if count == 0 and c == 'U': 
            res += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(raw_input().strip())

    path = raw_input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()


"""
JUMPING ON THE CLOUDS

There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.

Example: 
c = [0,1,0,0,0,1,0]
Index the array from 0...6. The number on each cloud is its index in the list so the player must avoid the clouds at indices 1 and 5. They could follow these two paths: 0 -> 2 -> 4 -> 6  or 0 -> 2 -> 3 -> 4 -> 6 . The first path takes 3 jumps while the second takes 4. Return 3.

Sample Input: 
7
0 0 1 0 0 1 0

Sample Output:
4
"""


import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jump = 0
    c. append(1)
    if len(c) < 3:
        return 0
    i = 0
    while i < len(c) -2:
        if c[i +2] == 0:
            i += 2
        else:
            i += 1
        jump += 1
    return jump    
    
"""
    jumps = 0
    current = 0

    while current < len(c):
        if current + 2 > len(c) and c [current + 2] == 0:
            jumps += 2
            current += 2
        elif current +1 < len(c) and c[current + 1] == 0:
            jumps += 1
            current += 1
        else:
            current += 1
"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()