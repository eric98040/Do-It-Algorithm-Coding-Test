import sys
input = sys.stdin.readline

n = int(input())
from queue import PriorityQueue
myQueue = PriorityQueue()
# x가 제일 작은거 -> abs(x)가 제일 작은 거 


for _ in range(n) : 
    x = int(input())
    
    if x!=0 : 
       myQueue.put((abs(x),x,x))
       
    else : 
        if myQueue.empty() : 
            print(0)
        else : 
            print(myQueue.get()[1])
            

            

        
        
