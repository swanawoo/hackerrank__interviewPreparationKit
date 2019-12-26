#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
	ar.sort()
	print(ar)
	result_cnt = 0
	prev_var = -1
	for cur_var in ar:
		if(prev_var<0): # first element of array
			pair_cnt = 1
		else:
			if(cur_var == prev_var):	
				if(pair_cnt == 1):
					result_cnt += 1				
					pair_cnt = 0
				elif(pair_cnt == 0):
					pair_cnt = 1
			else:
				pair_cnt = 1
		prev_var = cur_var
	return result_cnt

if __name__ == '__main__':
    fptr = sys.stdout # open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
