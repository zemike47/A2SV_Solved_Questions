def dfs(i, pos):
    global good, total

    if i == questions:
        global target
        total += 1

        if pos == target:
            good += 1
        return

    dfs(i + 1, pos + 1)
    dfs(i + 1, pos - 1)
# print(current)
dfs(0, current)

ans = good / total
print(f"{ans:.12f}")