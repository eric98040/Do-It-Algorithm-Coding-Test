# < Mysol > 

import sys
input = sys.stdin.readline

n  = int(input()) # 재료의 개수
m  = int(input()) # 갑옷을 만드는 데 필요한 수
array = sorted(list(map(int, input().split()))) # 재료들이 가진 고유한 번호

start = cnt = 0
end = n-1
tot = array[start] + array[end]

while start < end : 
    
    tot = array[start] + array[end]
    
    if tot < m : 
        start +=1
        
    elif tot > m : 
        end -=1
    
    else : 
        cnt+=1
        start+=1
        end-=1

print(cnt)

# <solution>

import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()
count = int(0)
i = int(0)
j = int(N-1)
while i < j:    # 투 포인터 이동 원칙 따라 포인터를 이동하며 처리
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1
print(count)
    



