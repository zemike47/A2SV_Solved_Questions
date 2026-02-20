n = int(input())
a = list(map(int,input().split()))
 
a.sort()

day = 1
i = 0

while i < len(a):
    if a[i] >= day:
        day += 1
        
    i += 1
    
    
 
print(day - 1)
