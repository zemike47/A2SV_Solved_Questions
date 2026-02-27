t = int(input())


for _ in range(t):
    n,k = map(int,input().split())
    s = input().strip()
    
    left = 0
    
    from collections import defaultdict
    
    window = defaultdict(int)
    ans = float("inf")
    
    for right in range(n):
        window[s[right]] += 1
        
        while sum(window.values()) == k:
            B = window['B']
            W = k - B
            
            ans = min(ans,W)
            
            window[s[left]] -= 1
            
            if window[s[left]] == 0:
                del window[s[left]]
            
            left += 1
    
    print(ans)
        
        
        
            
            
    
    
