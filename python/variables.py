# In Python, a variable is a name that refers to a value stored in the computer's memory.
# You can think of a variable as a container that holds data.
print("""
      Variable names can contain letters (a-z, A-Z), numbers (0-9), and underscores (_).
      They cannot start with a number and cannot contain spaces or special characters like !, @, #, $, etc.
      Variable names are case-sensitive, meaning myVar and myvar are different variables.
      To assign a value to a variable, use the assignment operator (=).
      Python is dynamically typed, which means you don't need to declare the type of a variable explicitly.
      The data type of a variable is determined based on the value assigned to it.

      """)
x = 10         # Integer
y = 3.14       # Float
name = "Alice" # String
is_valid = True  # Boolean
# Variable Reassignment:
x = 10
x = 20  # Now x is 20

# Multiple Assignments:
a, b, c = 1, 2, 3

# Variables in Python have a scope, which defines where they can be accessed.
# Global variables are accessible throughout the program, while local variables are confined to a specific block or function.
global_var = 100   # Global variable
def my_function():
    local_var = 200  # Local variable
    global global_var; # This is the way to access global variable within function to be modified 
    # and used outside the scope of function. 

    global_var = global_var+1
    print(global_var)  # Accessing global variable
my_function() # 101 
my_function() # 102 

# Python does not support global variables, convention is to use with upper case 
PI = 3.14

# Python has several built-in data types for variables:
# Integers (int): Whole numbers without decimal points 
5, -10
# Floats (float): Numbers with decimal points 
3.14, -2.5
# Strings (str): Sequences of characters enclosed in quotes 
"hello", 'world'
# Booleans (bool): 
True,  False
# Lists (list): Ordered collections of items
[1, 2, 3]
# Tuples (tuple): Immutable ordered collections 
(1, 2, 3)
# Dictionaries (dict): Key-value pairs 
{'key': 'value'}
# Sets (set): Unordered collections of unique items 
{1, 2, 3}


# You can use the isinstance function to check if a variable is of a specific type.
x = 10
y = "hello"
print(isinstance(x, int))  # True
print(isinstance(y, int))  # False
print(isinstance(y, str))  # True

# Python provides built-in functions for type conversion:
# int(): Converts to an integer.
# float(): Converts to a float.
# str(): Converts to a string.
# bool(): Converts to a boolean.
num_str = "123"
num_int = int(num_str) # 123
print(num_int + 5)  # Output: 128 (since "123" converted to 123 as an integer)

x = 10
y = float(x)  # Casting integer to float  # 10.0
z = str(x)    # Casting integer to string # "10"

# -- Implicit Type Conversion:
num_int = 10
num_float = 3.5
result = num_int + num_float  # Implicitly converts num_int to float for addition
print(result)  # Output: 13.5

# PArsing user input 
# -- num_str = input("Enter a number: ")
# -- num_int = int(num_str)
x = None
print(type(x))  # Output: <class 'NoneType'>
# variable annotations like age: int = 30 are not strict type enforcement mechanisms. They are primarily used for readability and static type checking tools like MyPy.
age: int = 30
age="ss"
print(age)
# Primarily used for type hinting and do not enforce the type at runtime. 

def add_numbers(x: int, y: int) -> int:
    return x + y
print(add_numbers(1.2,1)) # 2.2 

x=10
print(type(x))  # Output: <class 'int'>

nums = [1, 2, 3]
a, b, c = nums  # Unpacking the list into variables a, b, and c
print(a,b,c) # 1 2 3


try: 
    x = 10
    del x  # Deletes the variable x
    print(x) # NameError: name 'x' is not defined
except NameError:
    print("Name Error as x is deleted ") # this will print.


from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
print(Color.RED) # Color.RED
print(Color.RED.name) # RED
print(Color.RED.value) # 1

# The is operator to check if two variables refer to the same object in memory.
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  # Output: False (different objects)
print(x is z)  # Output: True (same object) 

def my_function(*args, **kwargs):
    print(args)    # Tuple of positional arguments  # (1, 2, 3)
    print(kwargs)  # Dictionary of keyword arguments # {'name': 'Alice', 'age': 30}

my_function(1, 2, 3, name="Alice", age=30)
x: int = 10
y: float = 3.14
x = "nishant"
print(x) # nishant

def add_numbers(a: int, b: int) -> int:
    return a + b
print(add_numbers("nishant","saxena")) # nishantsaxena 

### Variable unpacking with * (Extended Unpacking):
nums = [1, 2, 3, 4, 5]
first, *rest = nums  # Unpacks the first element and collects the rest into a list
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4, 5]

# Multiple Assignments and Swapping:
a, b = 10, 20
a, b = b, a  # Swaps the values of a and b
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string) # My name is Alice and I am 30 years old.










