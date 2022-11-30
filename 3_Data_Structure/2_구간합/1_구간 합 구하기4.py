''' 3. 구간 합 구하기 4 '''

# <Mysol>
import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # n : 수의 개수, m : 합을 구해야 하는 개수

array = list(map(int,input().split()))
sums = [0]
temp = 0

# sums에 합 배열을 추가하기 : 1~len(array)만큼 모든 구간에 대한 합 배열을 구하기
for i in array : 
    temp+=i
    sums.append(temp)


for _ in range(m) : 
    a,b = map(int,input().split())
    print(sums[b]-sums[a-1])