#code calculates aspects of a paint job

#Prompts the user and return their input as a float

def getFloatInput(prompt_text):#defines getFloatInput function
 while True:
     try:
         #get user input and convert to float
         user_input= input(prompt_text)
         float_value = float(user_input)

         #make sure input is positive
         if float_value > 0:
             return float_value
         else:
             #if zero or negative, show error and repeat loop
             print('Input must be a positive numeric value')
     except ValueError:
         #if user enters text instead of numbers, show error
         print('Input must be a numeric value')
#prompt for square footage of wall
fWallSpace= getFloatInput('Enter wall space in square feet:') #prompt for price of the paint
fPaintPrice= getFloatInput('Enter paint price per gallon:')
#prompt for feet per gallon of paint
fFeetPerGallon= getFloatInput('Enter feet per gallon of paint:')
#prompt for labor hours per gallon of paint
fLaborHoursPerGallon= getFloatInput('How many labor hours per gallon of paint:')
#prompt for labor charge per hours
fLaborChargePerHour= getFloatInput('Labor charge per hour:')
#prompt user for the state that the job is in
JobState= input('State the job is in (i.e. MA, CT, etc.):')
#prompt user for the customer's last name
CustomerLastName= input('Customer last name:')
#match tax rate to state entered by user
if JobState == 'CT':
     TaxRate= .06
elif JobState == 'MA':
     TaxRate= .0625
elif JobState == 'ME':
     TaxRate= .085
elif JobState == 'NH':
     TaxRate= 0
elif JobState == 'RI':
     TaxRate= .07
elif JobState == 'VT':
     TaxRate= .06
else:
     TaxRate= 0

import math
#calculate gallons of paint
def getGallonsOfPaint(fWallSpace,fFeetPerGallon):
     fTotalGallons= fWallSpace / fFeetPerGallon
     iTotalGallons= math.ceil(fTotalGallons)
     return int(iTotalGallons)
#calculate hours of labor
def getLaborHours(fLaborHoursPerGallon,iTotalGallons):
     fLaborHours= fLaborHoursPerGallon*iTotalGallons
     return float(fLaborHours)
#calculate cost of labor
def getLaborCost(fLaborHoursPerGallon,fLaborChargePerHour):
     fLaborCost= fLaborHoursPerGallon*fLaborChargePerHour
     return float(fLaborCost)
 #calculate cost of paint
def getPaintCost(iTotalGallons,fPaintPrice):
     fPaintCost= iTotalGallons*fPaintPrice
     return float(fPaintCost)
#calculate sales tax
def getSalesTax(TaxRate,fPaintCost,fLaborCost):
     fTax= TaxRate*(fPaintCost+fLaborCost)
     return float(fTax)
#calculate total cost
def showCostEstimate(iTotalGallons,fLaborHours,fLaborCost,fPaintCost,fTax):
     fTotalCost= fLaborCost+fPaintCost+fTax
#print all of the outputs
print('Gallons of paint: ',iTotalGallons)
print('Hours of labor: ',fLaborHours)
print('Paint charges: ',fPaintCost)
print('Labor charges: ',fLaborCost)
print('Tax: ',fTax)
print('Total cost: ',fTotalCost)
     
CustomerLastName.write('Gallons of paint: ',iTotalGallons\n)
CustomerLastName.write('Hours of labor: ',fLaborHours)
CustomerLastName.write('Paint charges: ',fPaintCost)
CustomerLastName.write('Labor charges: ',fLaborCost)
CustomerLastName.write('Tax: ',fTax)
CustomerLastName.write('Total cost: ',fTotalCost))





#create text file with all of the outputs formatted in it
#output to a file (CustomerLastName_PaintJobOutput.txt)
#output message saying that a file was created and show file name
# File: (filename) was created.



