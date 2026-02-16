
t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    answer = float('inf')
    
    for i in range(n):
        a = b = c = 0
        
        # check substrings of length 2 to 7
        for length in range(1, 8):
            if i + length > n:
                break
            
            char = s[i + length - 1]
            
            if char == 'a':
                a += 1
            elif char == 'b':
                b += 1
            else:
                c += 1
            
            if length >= 2:
                if a > b and a > c:
                    answer = min(answer, length)
    
    print(answer if answer != float('inf') else -1)
