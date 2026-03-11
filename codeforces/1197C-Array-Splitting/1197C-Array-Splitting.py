# base cost (no split)
total = a[-1] - a[0]

# compute gaps
gaps = []
for i in range(n-1):
    gaps.append(a[i+1] - a[i])

# choose largest gaps
gaps.sort(reverse=True)

# subtract the biggest k-1 gaps
for i in range(k-1):
    total -= gaps[i]

print(total)