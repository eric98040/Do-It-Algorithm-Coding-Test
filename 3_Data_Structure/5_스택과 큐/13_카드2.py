import sys
input = sys.stdin.readline

n = int(input())
from collections import deque

array = deque(range(1,n+1))

while len(array) > 1 : 
    array.popleft()
    array.append(array.popleft())
    
print(array[0])
