num=int(input("enter the number:"))
reversed_num=0
while num>0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num=num//10
print("the reversed_number is:",reversed_num)
