# 2. 평균구하기

# <Mysol>

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))

print(100/max(array) * sum(array)/n)

    