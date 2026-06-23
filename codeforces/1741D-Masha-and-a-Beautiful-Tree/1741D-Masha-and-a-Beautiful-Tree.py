def merge(left, right):
    global cnt

    if left[0] > right[0]:
        cnt += 1
        return right + left
    else:
        return left + right


def mergesort(l, r, arr):
    if l == r:
        return [arr[l]]

    mid = (l + r) // 2

    left = mergesort(l, mid, arr)
    right = mergesort(mid + 1, r, arr)

    return merge(left, right)


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = 0

    if n == 1:
        print(0)
        continue

    result = mergesort(0, n - 1, arr)

    if result == sorted(arr):
        print(cnt)
    else:
        print(-1)