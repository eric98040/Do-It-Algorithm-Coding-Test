# < Mysol1 >

# import sys
# input = sys.stdin.readline

# size = int(input())
# from collections import deque

# array = deque(list(map(int,input().split())))

# while array : 
#     x = array.popleft()
#     for i in array :
#         if i>x : 
#             print(i,end = ' ')
#             break
#     else : 
#         print(-1, end = ' ')
        
        
# < Mysol2 > 

# https://hooongs.tistory.com/329 참고


import sys
input = sys.stdin.readline

size = int(input())

array = list(map(int,input().split()))
res = [-1] *(size)
stack = []

for idx,i in enumerate(array) :
    
        while stack and i>stack[-1][1] : 
            
            index_num, value = stack.pop()
            res[index_num] = i
            
        stack.append([idx,i])
        
print(*res)

# < Mysol3 - re >

# 수열의 크기 N이 최대 1,000,000개 이므로 O(N)알고리즘을 사용해야 함

import sys
input = sys.stdin.readline

size = int(input())
array = list(map(int, input().split()))
stack = [array[0]]

for i in range(1,size) : 
    
    if array[i] > stack[-1] : 
        print(array[i], end = ' ')
        stack.pop()
        stack.append(array[i])
        
    else : 
        pass
        
            
            





