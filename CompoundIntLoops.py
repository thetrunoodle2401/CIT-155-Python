#Calculate Compound Interest with Loops
 
fDeposit=0 #define
while fDeposit <1:#validate the input
    try:
        fDeposit= float(input('What is the Original Deposit (positive value): '))#prompt user for deposit
        if fDeposit <=0:#correct user input
            print('Input must be a positive numeric value')
    except ValueError:
        print('Input must be a numeric value')
    #repeats prompt until the input matches the criteria

fInterest_Rate=0 #define
while fInterest_Rate <1:#validate the input
    try:
        fInterest_Rate = float(input('What is the Interest Rate (positive value): '))#prompt user for interest rate percentage
        if fInterest_Rate <=0:#correct user input
            print('Input must be a positive numeric value')
    except ValueError:
        print('Input must be a numeric value')
    #repeats prompt until the input matches the criteria

#prompt for number of months
iMonths=0 #define
while iMonths<1:#validate the input
    try:
        iMonths = int(input('What is the Number of Months (positive value): ')) #prompt user for deposit
        if iMonths<=0:#correct user input
            print('Input must be a positive numeric value')
    except ValueError:
        print('Input must be a numeric value')
    #repeats prompt until the input matches the criteria

fGoal=0 #define
while fGoal<=0:#validate the input
    try:
        fGoal = float(input('What is the Goal Amount (can enter 0 but not negative): '))#prompt for goal
        if fGoal <0:#correct user input
            print('Input must be 0 or greater')
    except ValueError:
        print('Input must be a numeric value')
    #repeats prompt until the input matches the criteria

#convert interest percentage to decimal and divide interest rate by 12 for monthly rate
fMonthly_Interest_Rate= (fInterest_Rate/100)/12


for num in range(1,iMonths+1): #calculate and show for the months entered
    fAccount_Balance=(fDeposit*fMonthly_Interest_Rate)*num+fDeposit
    format_fAccount_Balance= "{:.2f}".format(fAccount_Balance)
    #fAccount_Balance
    print('Month: ',num,'Account Balance is: $',format_fAccount_Balance)#Output the Month Number and the new Account Balance (formatted as currency) to the screen 
 #Repeat the loop until the number of months has been met.


while fAccount_Balance<fGoal:
     fAccount_Balance=(fDeposit*fMonthly_Interest_Rate)*num+fDeposit
     num+=1
print('It will take',num,'months to reach the goal of $',fGoal)
