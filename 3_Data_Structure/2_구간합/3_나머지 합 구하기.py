
''' 5. 나머지 합 '''
   
# hint :

# (a+b)%c = ((a%c) + (b%c))%c 와 같음
# 특정 구간 수들의 나머지 연산을 더해 나머지 연산을 한 값과 이 구간 합의 나머지 연산을 한 값은 동일
# (S[i] - S[j-1]) % M = (a[j] + a[j+1] + .... + a[i]) % M = (a[j]%M + a[j+1]%M + .... + a[i]%M) % M = (S[i]%M - S[j-1]%M) %M
# 즉, (S[i] - S[j-1]) % M = (S[i]%M - S[j-1]%M) %M : 부분합 리스트의 각 원소를 M으로 미리 나누고 시작

# S[i]%M의 값과 S[j]%M의 값이 같다면 (S[i]-S[j]) % M은 0이다.
# 1. 구간 합 배열의 원소를 M으로 나눈 나머지로 업데이트 
# 2. S[i], S[j]가 같은 (i,j)쌍을 찾으면 원본 리스트에서 j+1 ~ i까지의 구간 합이 M으로 나누어 떨어짐

      
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
array = list(map(int, input().split()))

sums = [0]
temp = 0
dp = [0] *(m+1)
res = 0 # 맨 앞에 있는 0 하나 제거 필요

# 합 배열 구하기
for i in array :
    temp+=i
    sums.append(temp)
    
# for i in range(1,n+1) : 
#     sums[i] = sums[i-1] + array[i-1]

# 합 배열의 각 원소들을 m으로 나눠주기 
for i in range(n+1) : 
    sums[i]%=m

# Brute force 방식보다 Dynamic programming 방식이 더 빠름

# 답 : 각 원소들이 나오는 횟수 = n -> nC2의 합
for i in sums : 
    dp[i]+=1

for j in dp : 
    res+=(j*(j-1))//2
    
print(res)
    
    