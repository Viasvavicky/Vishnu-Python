a = [[2, 1], [1, 1]]
b = [[2, 3], [1, 4]]
ans=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(a)):
            ans[i][j] += a[i][k] * b[k][j]
print(ans)
