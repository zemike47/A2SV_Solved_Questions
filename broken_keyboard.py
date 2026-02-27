t = int(input())

for _ in range(t):
    s = input().strip()
    i = 0
    res = set()
    
    while i < len(s):
        j = i
        
        # count consecutive equal letters
        while j < len(s) and s[j] == s[i]:
            j += 1
        
        block_length = j - i
        
        if block_length % 2 == 1:
            res.add(s[i])
        
        i = j   # move to next block
    
    print("".join(sorted(res)))
