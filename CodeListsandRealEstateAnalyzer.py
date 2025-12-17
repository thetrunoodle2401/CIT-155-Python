 #this is a sales analyzer program for real estate sales  

def getFloatInput(prompt_text):#define getFloatInput function
 while True:
     try:
         #get user input and convert to float
         user_input= input(prompt_text)
         float_value = float(user_input)

         #make sure input is positive
         if float_value > 0:
             return float_value #Return a valid non-zero float.

         else:
             #if zero or negative, show error and repeat loop
             print('Input a number that is greater than 0')
     except ValueError:
         #if user enters text instead of numbers, show error
         print('Input must be a number')
   
def getMedian(value_list):
    list_length= len(value_list)#determine length of list
    mid_index = list_length // 2 #find middle item
    if list_length % 2 == 1:#odd number of items
       median_value= float(value_list[mid_index])#determine median
    else:#even number of items
        median_value= (value_list[mid_index-1]+value_list[mid_index])/2.0 #calculate median by averaging the two middle items
    return median_value
    
#create a main function
def main():

    #create empty list
    value_list=[]

    #make variable to control loop
    MoreValues= 'y'

    while MoreValues in ('Y','y'):
        #Prompt for property sales value
        fSalesValue= getFloatInput('Enter property sales value:')
        #Use list to store all the user inputted sales values.
        value_list.append(fSalesValue)
        while True:#input validation loop
            #prompt for if the user wants to add another value
            MoreValues=input('Enter another value? Y or N:')
            #repeat until N or n is entered
            if MoreValues in ('y','Y','n','N'):
                break
            else:
                print('Please enter a Y, y, N, or n')
    
    #Sort the list from smallest value to largest.
    value_list.sort()
    
    #Output each entry in the sorted list
    prefix= 'Property' #format output stuff
    for index, item in enumerate(value_list,start=1):
        output = "{0}  {1}   $ {2:,.2f}".format(prefix, index, item)
        #output= prefix +'  ' + str(index) + '   $ ' + str(item)
        print(output)
   
    #Determine the Minimum value and output formatted
    fMinimum= min(value_list)
    format_fMinimum="{:,.2f}".format(fMinimum)
    print('Minimum: $',format_fMinimum)

    #Determine the Maximum value and output formatted
    fMaximum= max(value_list)
    format_fMaximum="{:,.2f}".format(fMaximum)
    print('Maximum: $',format_fMaximum)

    #Determine the Total value and output formatted
    fTotal= sum(value_list)
    format_fTotal="{:,.2f}".format(fTotal)
    print('Total: $',format_fTotal)

    #add list items together
    fAdded = sum(value_list)
    #count number of items in list
    fCount = len(value_list)
    #Calculate the Average 
    fAverage = fAdded / fCount
    #Output the average formatted
    format_fAverage="{:,.2f}".format(fAverage)
    print('Average: $',format_fAverage)

    #Find the Median using the getMedian function 
    fMedian= getMedian(value_list)
    #format and print
    format_fMedian="{:,.2f}".format(fMedian) 
    print('Median: $',format_fMedian)

    #calculate commission
    fCommission= fTotal * .03
    #format and print 
    format_fCommission="{:,.2f}".format(fCommission)
    print('Commission: $',format_fCommission)

 #call the main function
if __name__ == "__main__":
    main()
