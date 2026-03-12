s = input()

stack = [-1]
max_length = 0
count_valids = 0

for i in range(len(s)):
        
    if s[i] == "(":
        stack.append(i)
    else:
        stack.pop()
        
        if not stack:
            stack.append(i)
        
        else:
            
            length = i - stack[-1]
            
            if length > max_length:
                max_length = length
                count_valids = 1
                
            elif length == max_length:
                count_valids += 1
                

if max_length == 0:
    count_valids = 1
            
print(max_length,count_valids)