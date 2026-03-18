t = int(input())

for _ in range(t):
    s = list(input().strip())
    t_str = list(input().strip())

    for i in range(len(s)):
        if s[i] not in t_str:
            print("Impossible")
            break
        else:
            t_str.remove(s[i])
    else:
                
        sorted_t = sorted(t_str)
        
        lt,ls = 0,0
        ans = []
        
        while lt < len(sorted_t) and ls < len(s):
            if sorted_t[lt] < s[ls]:
                ans.append(sorted_t[lt])
                lt += 1
            else:
                ans.append(s[ls])
                ls += 1
                
        if lt < len(sorted_t):
            ans.extend(sorted_t[lt:])
        
        if ls < len(s):
            ans.extend(s[ls:])
            
        print("".join(ans))