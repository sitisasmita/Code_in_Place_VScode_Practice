#CONSTANT VARIABLE
MAX_NUMBER = 20

#even number function
def even_odd_num(): #named a variable with a descriptive name
    for num in range(MAX_NUMBER):
        #if num % 2 return remainder number = 0, it means num is even number
        if num % 2 == 0:
            print(num, "is even number")
        else: #when num % 2 is not 0, it means num is odd number
            print(num, "is odd number")

#call function 
even_odd_num()

"""
How to run this program ?,
    1. Click Terminal
    2. Click New Terminal
    3. in Windows type : py (file_name.py)
                  e.g. : py even_odd_number.py
       hit enter
    
    if you want to clear terminal, just type clear and hit enter
"""