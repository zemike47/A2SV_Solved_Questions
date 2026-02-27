
n,k = map(int,input().split())

arr = list(map(int,input().split()))


from collections import defaultdict

freq_map = defaultdict(int)
distnict = 0
ans = 0 
left = 0 

for right in range(n):
    
    freq_map[arr[right]] += 1
        
    while len(freq_map) > k:
        freq_map[arr[left]] -= 1
        
        if freq_map[arr[left]] == 0:
            del freq_map[arr[left]]
        
        left += 1
        
    ans += right - left + 1

print(ans) 
        
        
        
        
        
        
    
        
        

    
     
    
    
    
    
    
    
