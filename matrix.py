a=[[2,1],[3,4]]
res=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(i):
        res[i][j]=a[j][i]
print(res)
