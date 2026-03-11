t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    
    
    rprefix = []
    raccumulator = 0
    
    for i in range(n):
        raccumulator += r[i]
        rprefix.append(raccumulator)
        
    
    bprefix = []
    baccumulator = 0
    
    for i in range(m):
        baccumulator += b[i]
        bprefix.append(baccumulator)
    
    m1 = max(rprefix)
    mred = max(0,m1)
    m2 = max(bprefix)
    mblue = max(0,m2)
    
    
    print(mred+mblue)