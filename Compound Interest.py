#calcuates compound interest

# get input for amount of principal originally deposited in the account
PV = float(input("Enter the starting pricipal: "))

# get input for annual interest rate paid by the account
R = float(input("Enter the annual interest rate: "))

#turn rate from percentage to decimal
r = R/100

# get input for number of times per year that the interest is compounded (ex. monthly = 12, quarterly = 4)
m= float(input('How many times per year is the interest compounded? '))

# get input for number of years the account will be left to earn interest
t= float(input('For how many years will the account earn interest? '))

#calculate and display the amount of money that will be in the account after the specified number of years

FV = PV*(1 + r/m)**(m*t)
format_FV="{:,.2f}".format(FV)
print('At the end of',t,'years you will have $',format_FV)