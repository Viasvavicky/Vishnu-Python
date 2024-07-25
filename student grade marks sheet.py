n1= int(input("Enter the marks: "))
n2=int(input("enter the marks:"))
n3=int(input("enter the marks:"))
n=(n1+n2+n3)/3     
if 80<n<=100:
    print("The grade is A")
elif 60 < n <= 80:
    print("The grade is B")
elif 50 < n<= 60:
    print("The grade is C")
else:
    print("Fail")
