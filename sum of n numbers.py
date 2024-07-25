n=int(input("enter the number"))
sum=0
for i in range(1,n+1):
    for j in range(i,i+1):
        sum=sum+i
print("the sum of {n} numbers is:",sum)
