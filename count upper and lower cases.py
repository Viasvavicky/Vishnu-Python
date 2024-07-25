string=input("enter the string:")
ucount=0
lcount=0
space=0
for i in string:
    if(i.islower()):
        lcount=lcount+1
        if(i.isupper()):
            ucount=ucount+1
        else:
            space=space+1
print("the lower count is:",lcount)
print("the uppwer count is:",ucount)
print(space)
                
            
