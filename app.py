"""

This is a mulit-line comment / string
Welcome to python 101

"""

# this is a commment

"""
 - single comments & multi-line comment/ string
 - variable (hold references to what has been stored in memory. It can only be used after defined)
"""
name = "John Doe" # this is a variable
name = "Peter Jane" # this is called variable overriding
output =""
age = 12
weight = 12.4

output = age
output = weight


# DATA-TYPES: TEXT | NUMBERS | LISTS 
""" 
NUMBERS: 
    - integer: values that span from 0 ->  infinity and 0 -> -ve infinity, DO NOT HAVE decimals. 
    integers have a class int()

    - float: values that have decimals. Have a class of float()

    - complex: sqaure-root of -2 => complex number. Have a class of complex().
    in complex numbers we use the keyword j after the number

"""
numberOne = 10 # integer
output = numberOne # returns the value of number One
output = type(numberOne) # returns the data type

weightOne = 20.5 # floating 
output = weightOne # returns the value of weightOne
output = type(weightOne) # returns the data type

complexNumberOne = 2j # complex
output = complexNumberOne # returns the value of complexNumberOne
output = type(complexNumberOne) # returns the data type

numberOne = 12
output = float(numberOne) # it parsing the value to a floating point number
output = int(numberOne) # it has parsed the value back to integer
output = complex(numberOne) # it is being parsed to a complex number

"""
Operators & Operands:
    e.g. x + y = 10 .... find x : x and y are called operands and + and = are called operators
    - operators: 
        +(add)
        -(minus) 
        /(division)
        //(floor division)
        *(multiplication)
        **(power) 
        %(modulus)
"""

numberOne = 10
numberTwo = 20
# numberTwo = 3 # overrided the value of numberTwo

output  = numberOne + numberTwo # addition 
output  = numberOne + numberTwo # addition
output  = numberOne / numberTwo # division
output  = numberOne // numberTwo # floor division => truncates
output  = numberOne * numberTwo # mulitiplication
output  = numberOne ** numberTwo # power 
numberTwo = 3
numberTwo = 7
output  = numberOne % numberTwo # modulus => returns the remainder



print("===============================")
print(output)
print("===============================")