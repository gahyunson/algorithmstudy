#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nimbleGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
"""
N개의 상자가 있다.
각 상자에는 C_i개 돌이 있다.
2명의 플레이어가 번갈아가며 플레이 한다.
각 차례에서 돌 1개만 선택해 선택한 상자보다 앞의 순서의 상자로 이동시킨다.
먼저 조작할 수 없게 되면 진다.
"""



def nimbleGame(s):
    # Write your code here
    cnt = 0
    for i in s:
        if i==0:
            cnt+=1
        else:
            pass
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = nimbleGame(s)
        if result==len(s):
            fptr.write("Second" + '\n')
        else:
            fptr.write("First"+'\n')

    fptr.close()
