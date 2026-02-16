import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()

    # Step 1: Find first time hitting 0 starting from x
    pos = x
    first_hit = -1

    for i in range(n):
        if s[i] == 'L':
            pos -= 1
        else:
            pos += 1

        if pos == 0:
            first_hit = i + 1
            break

    # If never hits 0 or happens after k seconds
    if first_hit == -1 or first_hit > k:
        print(0)
        continue

    # We hit 0 once
    count = 1
    remaining = k - first_hit

    # Step 2: Find cycle length starting from 0
    pos = 0
    cycle_length = -1

    for i in range(n):
        if s[i] == 'L':
            pos -= 1
        else:
            pos += 1

        if pos == 0:
            cycle_length = i + 1
            break

    # If no cycle, it will never return again
    if cycle_length == -1:
        print(count)
    else:
        count += remaining // cycle_length
        print(count)
