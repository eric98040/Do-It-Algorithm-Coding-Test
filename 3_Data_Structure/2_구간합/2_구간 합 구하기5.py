''' 4. 구간 합 구하기 5 '''

# <Mysol>

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [ [0]*(n+1) for _ in range(n+1)]

for i in range(n) : 
    array = list(map(int,input().split()))
    for j in range(n) : 
        graph[i+1][j+1] = array[j]


# 합 배열 만들기 : 2차원 리스트

dp = [[0]*(n+1) for _ in range(n+1)]
temp1 = 0
temp2 = 0

# 1행, 1열 먼저 채우기
for i in range(n+1) : 
    temp1 += graph[1][i] # 1행 결정
    temp2+= graph[i][1] # 1열 결정
    dp[1][i] = temp1
    dp[i][1] = temp2
    
# 2차원 dp 점화식으로 채우기

for i in range(2,n+1) : 
    for j in range(2,n+1) : 
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + graph[i][j] - dp[i-1][j-1]

# dp table을 이용해서 구간합 구하기


for _ in range(m) : 
    x1,y1,x2,y2 = map(int, input().split())
    print(dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1])
    

# <Mysol2>


import sys
input = sys.stdin.readline

n,m = map(int, input().split())

# 2차원 배열로 행렬 matrix 입력받기
matrix = [list(map(int, input().split())) for _ in range(n)]

# 합 배열 넣을 dp table 만들기
dp = [ [0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1) : 
    for j in range(1,n+1) : 
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i-1][j-1]
        
for _ in range(m) : 
    x1,y1,x2,y2 = map(int, input().split())
    print(dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1])

