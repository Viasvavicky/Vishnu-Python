n=int(input("enter the number:"))
fact=1
sum=0
for i in range(1,n+1):
    fact=fact*i
    sum=sum+fact
    print("the sum of factorial of {n} numbers is:",sum)
