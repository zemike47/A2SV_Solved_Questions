import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    balance = 0
    good = [False]*n

    for i in range(n):
        if a[i] == '1':
            balance += 1
        else:
            balance -= 1
        
        if balance == 0:
            good[i] = True

    flip = 0
    possible = True

    for i in range(n-1, -1, -1):
        cur = a[i]

        if flip:
            cur = '1' if cur == '0' else '0'

        if cur == b[i]:
            continue

        if not good[i]:
            possible = False
            break

        flip ^= 1

    print("YES" if possible else "NO")