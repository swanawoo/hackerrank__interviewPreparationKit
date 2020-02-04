#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    mountain = 0
    valley = 0

    for i in range (0,n):
        #print(level)
        #print(s[i])
        if('U'==s[i]):
            if(level==-1):
                valley = valley + 1
            level = level +1
        else:
            level = level -1

        # if(i>1):
        #     if( level>1 and 'U'==s[i-2] and s[i-1]=='U' and 'D'==s[i]):
        #         mountain = mountain + 1
        #     if( level<-1 and 'D'==s[i-2] and s[i-1]=='D' and 'U'==s[i]):
        #         valley = valley + 1
    return valley


if __name__ == '__main__':
    fptr = sys.stdout # open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
