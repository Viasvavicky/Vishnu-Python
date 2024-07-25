def simple_intres1t(principle,rate,time):
    return(principle*rate*time)/100
principle=float(input("enter the principle amount:"))
rate=float(input("enter the rate of intrest:"))
time=float(input("enter the time in years:"))
print("simple intrest is:",simple_intrest(principle,rate,time))
