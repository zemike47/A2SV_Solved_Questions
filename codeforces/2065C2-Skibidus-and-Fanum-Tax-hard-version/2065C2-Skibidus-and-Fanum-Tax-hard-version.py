from bisect import bisect_left
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()

    prev = -10**18
    ok = True

    for x in a:
        best = float('inf')

        # Keep x
        if x >= prev:
            best = min(best, x)

        # Transform x -> b[j] - x
        idx = bisect_left(b, prev + x)

        if idx < m:
            best = min(best, b[idx] - x)

        if best == float('inf'):
            ok = False
            break

        prev = best

    print("YES" if ok else "NO")