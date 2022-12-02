# < Mysol>

import sys
input  = sys.stdin.readline

n,l = map(int, input().split()) # 윈도우의 크기 = L
array = list(map(int,input().split())) # n개의 수 

# Di = i-L+1번째 원소 ~ i번째 원소 (총 개수 L개)
from collections import deque
window = deque()
window.append((0,array[0]))


for idx,i in enumerate(array) : 

    while window and window[-1][1] >= array[idx] : 
    
        window.pop()
        
    window.append((idx,i))

    if window[-1][0] - window[0][0] >= l : # 슬라이딩 윈도우의 길이는 l을 넘어가면 안됨
            window.popleft()[1]

    print(window[0][1], end = ' ')  
    
    
# <Solution>

from collections import deque
N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i],i))
    if mydeque[0][1] <= i - L: # 범위에서 벗어난 값은 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0], end=' ')      
        

    

    
        
        







