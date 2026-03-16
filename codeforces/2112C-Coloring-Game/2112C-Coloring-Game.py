t  = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    Max_element = arr[-1]
    count = 0

    for k in range(2, n):
        i = 0
        j = k - 1

        while i < j:
            if arr[i] + arr[j] > arr[k] and arr[i] + arr[j] + arr[k] > Max_element:
                count += j - i
                j -= 1
            else:
                i += 1

    print(count)