r1 = list(map(int,input().split()))
r2 = list(map(int,input().split()))
r3 = list(map(int,input().split()))
r4 = list(map(int,input().split()))
r5 = list(map(int,input().split()))

matrix = []


matrix.append(r1)
matrix.append(r2)
matrix.append(r3)
matrix.append(r4)
matrix.append(r5)

r,c= 0 , 0

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            r,c = i+1, j+1
            break

ans = 0
ans += abs(3-r)
ans += abs(3-c)

print(ans)

        



