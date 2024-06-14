#make user input temperature in Fahrenheit
def fahrenheit_temp():
    input_f_temp = int(input("Enter the Fahrenheit temperature: ")) #'input' will return the value as a string, so we need to convert it to int

    #call conver_temp function to calculate the input given 
    calc = convert_temp(input_f_temp) # input_f_temp is the 'input given'/Argument = information that's given when you call it 

    #print the output on Terminal
    print(input_f_temp,"°F =",calc, "°C")


#convert the temperature > Fahrenheit to Celsius
# formula °F to °C > (°F − 32) × 5/9 = °C
def convert_temp(temp_in_f): # temp_in_f is 'input expected'/Parameter = the variable that you name your incoming information(e.g. incoming information from input_f_temp)
    #calculate it
    temp_in_c = (temp_in_f - 32) * 5/9
    temp_in_c = round(temp_in_c, 2) #returns a floating point number that is a rounded version of the specified number(temp_in_c), with the specified number of decimals(2 digit after comma)
    
    return temp_in_c #return the input value so we can call it in another function, in this case, it will return the value to 'calc' in fahrenheit_temp()
    

#call the function or else it won't showing anything in the terminal
"""
note for myself:
You don't need to call convert_temp() outside of the fahrenheit_temp function, 
since fahrenheit_temp() already calls it with the appropriate argument.
to make it simple you can think fahrenheit_temp() as the main function in this work
"""
fahrenheit_temp()
