
# 1. 숫자의 합 구하기

# < Mysol >
import sys 
input = sys.stdin.readline

numbers = int(input())
array = list(map(int,list(input().rstrip())))

print(sum(array))

# <Mysol2>

import sys 
input = sys.stdin.readline

numbers = int(input())
array = list(map(int,list(input())))

print(sum(array))