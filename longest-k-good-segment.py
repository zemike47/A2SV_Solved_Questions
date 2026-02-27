n , k = map(int,input().split())
a = list(map(int,input().split()))

from collections import defaultdict

freq_map = defaultdict(int)
left = 0
ans = float("-inf")
l =0 
r = 0

for right in range(n):
    freq_map[a[right]] += 1
    
    while len(freq_map) > k:
        freq_map[a[left]] -= 1
        
        if freq_map[a[left]] == 0:
            del  freq_map[a[left]]
        
        left += 1
        
    new_max = right - left + 1
    if new_max > ans:
        l = left
        r = right
        
    ans = max(ans, new_max)
    
print(l+1,r+1)
    
    
        
            
        
        
