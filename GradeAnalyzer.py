#This program is meant to take 3-4 test scores and average them to get a letter grade.

name = input("Name of the person we are calculating the grades for: ") #prompt user for student name

#Prompt the user for the person's 4 test scores- only accepting whole numbers
    #make sure each score isn't less than 0
# if a negative is put in, write this on the screen "Test scores must be greater than 0" 
	#use exit() function to end program
	
test_1 = int(input('Test 1: ')) #prompt for test score-only whole numbers
if test_1 < 0:
     print("Test scores must be greater than 0") #can't be negative
     exit()
test_2 = int(input('Test 2: ')) 
if test_2 < 0:
     print("Test scores must be greater than 0") 
     exit()
test_3 = int(input('Test 3: '))
if test_3 < 0:
     print("Test scores must be greater than 0") 
     exit()
test_4 = int(input('Test 4: ')) 
if test_4 < 0:
     print("Test scores must be greater than 0") 
     exit()

#prompt user asking if the lowest grade should be determined and dropped from the calculation

drop_grade = input('Do you wish to Drop the Lowest Grade Y or N? ') #prompt user

#make sure the value input is either Y or N 

if drop_grade != 'Y' and drop_grade !='N': #if not y or n
     print('Enter Y or N to Drop the Lowest Grade')
     exit()
elif drop_grade == 'Y': #if dropping
#calculate which score is lowest and average the other 3
     if test_1 < test_2 and test_1 < test_3 and test_1 < test_4:
         average = ((test_2) + (test_3) + (test_4)) / 3
     elif test_2 < test_1 and test_2 < test_3 and test_2 < test_4:
         average = ((test_1) + (test_3) + (test_4)) / 3
     elif test_3 < test_1 and test_3 < test_2 and test_3 < test_4:
         average = ((test_1) + (test_2) + (test_4)) / 3
     elif test_4 < test_1 and test_4 < test_2 and test_4 < test_3:
         average = ((test_1) + (test_2) + (test_3)) / 3

elif drop_grade == 'N': #if no dropping
     average = ((test_1) + (test_2) + (test_3) + (test_4)) / 4 #average all four

average_format = "{:.1f}".format(average) #format for 1 decimal point

print((name)+"\'s test average is: ", (average_format)) #show what their average grade is

 #calculate letter grade

if average >= 97.0:
	 print("Letter Grade for this test is: A+")
elif average >= 94.0 and average <= 96.9:
	 print("Letter Grade for this test is: A")
elif average >= 90.0 and average <= 93.9:
	 print("Letter Grade for this test is: A-")
elif average >= 87.0 and average <= 89.9:
	 print("Letter Grade for this test is: B+")
elif average >= 84.0 and average <= 86.9:
	 print("Letter Grade for this test is: B")
elif average >= 80.0 and average <= 83.9:
	 print("Letter Grade for this test is: B-")
elif average >= 77.0 and average <= 79.9:
	 print("Letter Grade for this test is: C+")
elif average >= 74.0 and average <= 76.9:
	 print("Letter Grade for this test is: C")
elif average >= 70.0 and average <= 73.9:
	 print("Letter Grade for this test is: C-")
elif average >= 67.0 and average <= 69.9:
	 print("Letter Grade for this test is: D+")
elif average >= 64.0 and average <= 66.9:
	 print("Letter Grade for this test is: D")
elif average >= 60.0 and average <= 63.9:
	 print("Letter Grade for this test is: D-")
elif average < 59.9:
	 print("Letter Grade for this test is: F")
