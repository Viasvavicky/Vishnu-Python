def compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time - principal
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
print("Compound Interest:", compound_interest(principal, rate, time))
