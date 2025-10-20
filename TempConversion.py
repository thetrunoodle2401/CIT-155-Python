#This program (hopefully) converts temperatures from celsius to fahrenheit and vice versa

print('Grace\'s Temp Converter:') #welcome message with my name

user_temp = float( input("Enter a temperature: ")) #prompt user for a temperature

temp_scale = input("Is the temp F for Fahrenheit or C for Celsius?") #prompt user for F or f for fahrenheit or C or c for celsius

#if something other than c or f is entered, say "Enter a F or C"

if  temp_scale == 'f': #check if Fahrenheit
	 if int(user_temp) >212:#check if within range
		 print("Temp can not be > 212")
	 else:
		 celsius=(5.0/9)*(int(user_temp) - 32)#calculate
		 celsius_format= "{:.1f}".format(celsius)#format to 1 decimal point
		 print("The Celsius equivalent is: ",(celsius_format))
elif  temp_scale == 'F':
     if int(user_temp) >212:#check if within range
         print("Temp can not be > 212")
     else:
         celsius=(5.0/9)*(int(user_temp) - 32)#calculate
         celsius_format= "{:.1f}".format(celsius)#format to 1 decimal point
         print("The Celsius equivalent is: ",(celsius_format))#print formatted answer
elif temp_scale == 'c': #check if Celsius
     if int(user_temp) >100:#check if within range
         print("Temp can not be >100")
     else:
         fahrenheit=((9.0/5.0)*int(user_temp)+32) #calculate
         fahrenheit_format= "{:.1f}".format(fahrenheit)#format to 1 decimal point
         print("The Fahrenheit equivalent is: ",(fahrenheit_format))#print formatted answer
elif temp_scale == 'C': #check if Celsius
     if int(user_temp) >100:#check if within range
         print("Temp can not be >100")
     else:
         fahrenheit=((9.0/5.0)*int(user_temp)+32)
         fahrenheit_format= "{:.1f}".format(fahrenheit)
         print("The Fahrenheit equivalent is: ",(fahrenheit_format))
else:
    print("Enter a F or C")