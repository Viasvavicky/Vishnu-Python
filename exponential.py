def expo(base,power):
    ans=1
    while power>0:
        ans=ans*2
        power=power-1
    return ans
print(expo(2,5))
