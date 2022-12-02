# < Mysol1 >

import sys
input = sys.stdin.readline

# s : DNA 문자열 길이, p : 부분 문자열의 길이 (sliding window 길이)
s, p = map(int, input().split())

# dna : DNA 문자열
dna = input().rstrip()

# 최소 개수 : A, C, G, T
min_nums = list(map(int, input().split()))

# dp table : 해당 슬라이딩 윈도우에서 A, C, G, T 개수
dp = [0] * 4

start = 0
end = p-1
cnt = 0

# 부분 문자열의 x번째 index의 값 확인 -> dp 갱신하는 함수

def check_add_x(array,x) :
    global dp 
    if array[x] == "A" : 
        dp[0]+=1
    elif array[x] == 'C' : 
        dp[1]+=1
    elif array[x] == 'G' : 
        dp[2]+=1
    else: 
        dp[3]+=1
        
def check_sub_x(array,x) :
    global dp 
    if array[x] == "A" : 
        dp[0]-=1
    elif array[x] == 'C' : 
        dp[1]-=1
    elif array[x] == 'G' : 
        dp[2]-=1
    else: 
        dp[3]-=1
        
# 유효한 비밀번호인지 확인하는 함수

def password() : 
  global dp,start,end,cnt
  
  for i in range(4) : 
        
    # 유효한 비밀번호가 아닐 때
    if dp[i] < min_nums[i] : 
        start+=1
        end+=1
        break
        
  # 유효한 비밀번호일 때    
  else :
    cnt+=1
    start+=1
    end+=1

# array를 1번째 부분 문자열로 설정
array = dna[0:p]

# dp table 갱신
for i in range(len(array)) : 
    check_add_x(array,i)

# 1번째 부분 문자열 cnt 체크
password()

# 2번째 부분 문자열부터 cnt 체크
while end < s :
    
    check_sub_x(dna,start-1)
    check_add_x(dna,end)
    password()
        
print(cnt)






# < Solution >

checkArr = [0] * 4 # 비밀번호 체크 리스트
myArr = [0] * 4 # 현재 상태 리스트
checkSecret = 0 # A, C, G, T 중 통과되는 문자 개수

# 함수 정의
def myadd(c): #새로 들어온 문자를 처리하는 함수
    global checkArr,myArr,checkSecret
    if c == 'A':
        myArr[0] += 1
        if myArr[0] == checkArr[0]:
            checkSecret += 1
    elif c == 'C':
        myArr[1] += 1
        if myArr[1] == checkArr[1]:
            checkSecret += 1
    elif c == 'G':
        myArr[2] += 1
        if myArr[2] == checkArr[2]:
            checkSecret += 1
    elif c == 'T':
        myArr[3] += 1
        if myArr[3] == checkArr[3]:
            checkSecret += 1

def myremove(c): #제거되는 문자를 처리하는 함수
    global checkArr, myArr, checkSecret
    if c == 'A':
        if myArr[0] == checkArr[0]:
            checkSecret -= 1
        myArr[0] -= 1
    elif c == 'C':
        if myArr[1] == checkArr[1]:
            checkSecret -= 1
        myArr[1] -= 1
    elif c == 'G':
        if myArr[2] == checkArr[2]:
            checkSecret -= 1
        myArr[2] -= 1
    elif c == 'T':
        if myArr[3] == checkArr[3]:
            checkSecret -= 1
        myArr[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkArr = list(map(int, input().split()))

for i in range(4):
    if checkArr[i] == 0:
        checkSecret += 1
        
for i in range(P):  #초기 P 부분 문자열 처리 부분
    myadd(A[i])
    
if checkSecret == 4: #4자릿수와 관련된 크기가 모두 충족될 때 유효한 비밀번호
    Result += 1
    
for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    
    if checkSecret == 4:
        Result += 1
        
print(Result)