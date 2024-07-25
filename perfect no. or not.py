x=int(input("enter the number"))
total=0
for i in range(1,x):
    if x%i==0:
        total=total+i
if total==x:
   print("yes the given number is perfect number")
else:
    print("no the given number is not a perfect number")            
