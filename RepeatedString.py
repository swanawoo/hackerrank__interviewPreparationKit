#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
	a_per_string = s.count('a')
	no_of_multiply = int(n/len(s))

	result_cnt = a_per_string*no_of_multiply
	result_cnt += s[0:n-len(s)*no_of_multiply].count('a')
	
	return result_cnt
if __name__ == '__main__':
    fptr = sys.stdout # open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
