#code calculates aspects of a paint job


import math #make sure math things work

#Prompts the user and return their input as a float
def getFloatInput(sPromptText):#defines getFloatInput function
 while True:
     try:
         #get user input and convert to float
         sUserInput= input(sPromptText)
         fValue = float(sUserInput)

         #make sure input is positive
         if fValue > 0:
             return fValue
         else:
             #if zero or negative, show error and repeat loop
             print('Input must be a positive numeric value')
     except ValueError:
         #if user enters text instead of numbers, show error
         print('Input must be a numeric value')

# gallons of paint
def getGallonsOfPaint(fWallSpace,fFeetPerGallon):
    return math.ceil(fWallSpace / fFeetPerGallon)
# hours of labor
def getLaborHours(fLaborHoursPerGallon,iTotalGallons):
    return float(fLaborHoursPerGallon*iTotalGallons)
# cost of labor
def getLaborCost(fLaborHours,fLaborChargePerHour):
    return float(fLaborHours*fLaborChargePerHour)
     # cost of paint
def getPaintCost(iTotalGallons,fPaintPrice):
    return float(iTotalGallons*fPaintPrice)
# sales tax
def getSalesTax(fTaxRate,fPaintCost,fLaborCost):
     return float(fTaxRate*(fPaintCost+fLaborCost))

# total cost
def showCostEstimate(fLaborCost,fPaintCost,fTax):
    return float (fLaborCost+fPaintCost+fTax)
    

def main():
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
     sJobState= input('State the job is in (i.e. MA, CT, etc.):')
     #prompt user for the customer's last name
     sCustomerLastName= input('Customer last name:')

     if sJobState == 'CT':
         fTaxRate= .06
     elif sJobState == 'MA':
          fTaxRate= .0625
     elif sJobState == 'ME':
       fTaxRate= .085
     elif sJobState == 'NH':
          fTaxRate= 0
     elif sJobState == 'RI':
        fTaxRate= .07
     elif sJobState == 'VT':
         fTaxRate= .06
     else:
         fTaxRate= 0

     #calculations
     iTotalGallons= getGallonsOfPaint( fWallSpace , fFeetPerGallon)
     fLaborHours= getLaborHours(fLaborHoursPerGallon,iTotalGallons)
     fPaintCost= getPaintCost(iTotalGallons,fPaintPrice)
     fLaborCost= getLaborCost(fLaborHours,fLaborChargePerHour)
     fTax= getSalesTax(fTaxRate,fPaintCost,fLaborCost)
     fTotalCost= showCostEstimate(fLaborCost,fPaintCost,fTax)
     
     #format
     format_fPaintCost="{:,.2f}".format(fPaintCost)
     format_fLaborCost="{:,.2f}".format(fLaborCost)
     format_fTax="{:,.2f}".format(fTax)
     format_fTotalCost="{:,.2f}".format(fTotalCost)

     #print all of the outputs
     print('Gallons of paint: ',iTotalGallons)
     print('Hours of labor: ',fLaborHours)
     print('Paint charges: $',format_fPaintCost)
     print('Labor charges: $',format_fLaborCost)
     print('Tax: $',format_fTax)
     print('Total cost: $',format_fTotalCost)

     #create file
     filename= sCustomerLastName + '_PaintJobOutput.txt'
     
     with open(filename, 'w') as outFile:
         #write information to the file     
         outFile.write('Gallons of paint: ' + str(iTotalGallons) +  '\n')
         outFile.write('Hours of labor: ' + str(fLaborHours) + '\n')
         outFile.write('Paint charges: $' + str(format_fPaintCost) + '\n')
         outFile.write('Labor charges: $' + str(format_fLaborCost) + '\n')
         outFile.write('Tax: $' + str(format_fTax) + '\n')
         outFile.write('Total cost: $' + str(format_fTotalCost) + '\n')

     #print file confirmation
     print('File: ',filename,'has been created')

 #call the main function
if __name__ == "__main__":
    main()

   



