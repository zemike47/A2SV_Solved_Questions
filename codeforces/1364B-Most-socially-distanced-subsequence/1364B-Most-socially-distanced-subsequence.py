import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    # ans = [p[0]]

    # for i in range(1, n-1):
    #     if (p[i] - p[i-1]) * (p[i+1] - p[i]) < 0:
    #         ans.append(p[i])
    
    ans = []
    
    l = 0 
    
    while l < n - 1:
        ans.append(s[l])
        
        r = l + 1
        
        if s[l] > s[r]:
            while r < n - 1 and s[r] >= s[r+1]:
                r += 1 
            
        else:
            while r < n - 1 and s[r] < s[r+1]:
                r += 1
        
        l = r 
    
    ans.append(s[-1])
        
        
    print(len(ans))
    print(*ans)