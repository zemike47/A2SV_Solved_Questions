# n,m = map(int,input().split())

# arr1 = list(map(int,input().split()))
# arr2 = list(map(int,input().split()))


# from collections import Counter

# cntr_arr1 = Counter(arr1)
# cntr_arr2 = Counter(arr2)

# ans = 0

# for key in cntr_arr1:
#     if key in cntr_arr2:
#         k = cntr_arr1[key] * cntr_arr2[key]
#         ans += k

# print(ans)

ans = 0  

n,m = map(int,input().split())

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))  

i , j = 0 , 0

while i < n and j < m:
    if  arr1[i] < arr2[j]:
        i += 1    
    elif arr1[i] > arr2[j]:
        j += 1
    else:
        value = arr1[i]
        cnt_a = 0
        cnt_b = 0
        
        while i < n and arr1[i] == value:
            cnt_a += 1
            i += 1
            
        while j < m and arr2[j] == value:
            cnt_b += 1
            j += 1
        
        ans += cnt_a * cnt_b
    
print(ans)
        
        
        
        
        
        
              
        
        
