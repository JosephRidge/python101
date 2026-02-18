"""
This is a mulit-line comment / string
Welcome to python 101

"""

# this is a single line commment

"""
 - single comments & multi-line comment/ string
 - variable (hold references to what has been stored in memory. It can only be used after defined)
"""
name = "John Doe" # this is a variable
name = "Peter Jane" # this is called variable overriding
output ="" # global variable
age = 12
weight = 12.4

# variable overriding => we reassign the value of the variable
output = age
output = weight


# DATA-TYPES: TEXT | NUMBERS | LISTS 
"""
DATA TYPES: 
    - Text: str() -> list of characters enclosed inside quotation marks(either '' or ""). 
    - Numbers: int(), complex(), float() 
    - Lists: array, set, tuple, dictionary

"""

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


# userMathProblem = input("Hey, kindly input the problem you would like us to solve: ")
# output = eval(userMathProblem) # execute python scripts but has no control over which python scripts not to execute -> opens doors to possible malicious attacks


"""
COMPARISON OPERATORS: 
     - Answer the question: How does a compare with b? are they equal? 
      Is one smaller or bigger? or are they less than or equal to or greater than or equal to?
      - greater than (>)
      - less than(<)
      - greater than or equal to (>=)
      - less than or equal to (<=)
      - equality (==)
"""
numberThree = 20 
numberFour = 40 
output = numberThree == numberFour # check for equality between numberThree and numberFour
output = numberThree > numberFour # check for whether numberThree is greater than numberFour
output = numberThree < numberFour # check for whether numberThree is less than numberFour
output = numberThree <= numberFour # check for whether numberThree is less than or equal to numberFour
output = numberThree >= numberFour # check for whether numberThree is greater than or equal to numberFour

# BOOLEAN OPERATORS: and, or, not
age = 18
height = 150

output = (age < 20 and height > 200)
output = (age < 20 or height > 200)
output = not(age < 20 or height > 200)
output = not(age < 20 and height > 200)

#  Assignment operators: +=, -=, /=, *=, //=, =

numberOne = 10
numberTwo = 11

output = numberOne + numberTwo
# numberOne += numberTwo
# numberOne *= numberTwo
# numberOne /= numberTwo
# numberOne //= numberTwo
# numberOne **= numberTwo
i = 0
# i = i+1
# i+=1

# identity(is ... is not ) & membership(in) operators
fruits = ['mangoe','banana','apple', 'watermelons']

output = 'apple' in fruits

# STRINGS: str() => placed inbetween '' or ""
name = "John-Doe"
bio = """
My name is JOhn Doe, I am a data scientist based in Kenya focusing on Health-care analytics.
My core tools of trade are  Python,  Streamlit, Pandas and Colan
"""

output = name
output = bio

output = name[5] # accessing string characters using the index (counting in computers start from 0 ... n-1)
output = name[-1]
output = name[0:6] # slicing 
output = name[2:8]
output= name[-1:]
output= name[4:]
name = "John Doe" # instance of the string class
output = name[0:8:2] # slicing with a step or 2

# strings methods
output = name.upper()
output = name.lower()
output = name.replace('o','u')


print("===============================")
print(output)
print("===============================")