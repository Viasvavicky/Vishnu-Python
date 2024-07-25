n=1
m=100
for x in range(n,m+1):
    for i in range(2,x):
        if x % i==0:
            break
        else:
            print(x)
