'''  6. 수들의 합5  '''

# < Mysol1 >

import sys
input = sys.stdin.readline

n = int(input())

end = 1
tot = 1
cnt = 0

for start in range(1,n+1) : 
    
    
    while start <= end and tot < n : 
        end+=1
        tot+=end
    if tot == n :
        cnt+=1
        
    tot-=start
    
print(cnt)


# <Mysol2>

import sys
input = sys.stdin.readline

n = int(input()) 

start = end = cnt = tot =1
# cnt가 1인 이유는 end == n이 될 때 count를 하지 않기 때문

while end < n : 
    
    if tot < n : 
        end+=1
        tot+=end
    elif tot > n : 
        tot-=start
        start+=1
    else : 
        cnt+=1
        end+=1
        tot+=end

print(cnt)




# < Solution1 > 


n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
        
    elif sum > n:
        sum -= start_index
        start_index += 1
        
    else:
        end_index += 1
        sum += end_index
        
print(count)