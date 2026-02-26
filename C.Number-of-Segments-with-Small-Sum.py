n,s = map(int,input().split())

arr = list(map(int,input().split()))

left = 0

segments = 0

window_sum = 0

for right in range(len(arr)):
    window_sum += arr[right]
    
    while window_sum > s:
        window_sum -= arr[left]
        left += 1
    
    segments += (right - left +1)

print(segments)
    
    
    
