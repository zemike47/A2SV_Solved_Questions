n = int(input())
arr = list(map(int,input().split()))

arr.sort()
ans = arr[(n-1)//2]

print(ans)
