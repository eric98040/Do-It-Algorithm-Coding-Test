# 리스트를 정렬 -> 두 포인터를 양쪽 끝에 배치 -> 
# -> 두 포인터의 합 == 특정 수가 될 때 cnt+=1 (특정 수는 for문으로 계속 돌림)

import sys
input = sys.stdin.readline

n = int(input()) # size
lst = sorted(list(map(int,input().split()))) # 리스트 정렬

cnt = 0

for i in range(n) : 
    
    start = 0
    end = n-1
    
    while start <  end : 
        
        if lst[i] > lst[start] + lst[end] : 
            start+=1
        elif lst[i] < lst[start] + lst[end] : 
            end-=1
        else : 
            if start != i and end != i:
                cnt+=1
                break
            else : 
                if start == i : 
                    start+=1
                else : 
                    end -=1
            
print(cnt)
            

