#!/usr/bin/env python
# coding: utf-8
topic
5. Functions

• Basics Defining function
• function call Return statement
• Function with parameter and without parameter
• Function parameters Call by value or call by reference local and global variable
• Recursion, Anonymous (lambda) function
• User define functions
• Examples
# 1. Basics of Defining a Function
# A function is a block of code that performs a specific task. It allows you to organize your 
# code into reusable pieces. In Python, you define a function using the def keyword.

# In[3]:


def greet():
    print("Hello!")


# # 2. Function Call and Return Statement
# Once a function is defined, you can use it by calling its name.
# 
# 
# If a function produces some output, 
# 
# 
# you can return that value using the return statement.

# In[6]:


def add_numbers(a, b):
    return a * b

result = add_numbers(3, 5)
print(result)  


# # 3. Function with Parameters and Without ParametersFunctions can take parameters, 
# 
# 
# which are like variables that you pass to the function.
# 
# 
# 
# These parameters can be used inside the function.

# # with parammeters

# In[3]:


def greet(name):   # with parammeters
    print(f"Hello, {name}!")

greet("Alice")  


# # # withaout parammeters

# In[5]:


## withaout parammeters
def say_hello():
   print("Hello!")

say_hello()  # Output will be "Hello!"


# # 4. Function Parameters: Call by Value or Call by Reference, Local and Global Variables
# In Python, everything is passed by value, but for objects (like lists or dictionaries), the "value" is actually a reference to the object.
# 
# 
# Local variables are defined within a function and can only be used inside that function.
# 
# 
# Global variables are defined outside of any function and can be used anywhere in the code.

# In[7]:


global_var = 10

def my_function():
    local_var = 20
    print(f"Local variable: {local_var}")
    print(f"Global variable: {global_var}")

my_function()
print(f"Global variable outside function: {global_var}")


# In[6]:


fruit_name = "Apple"

def print_fruit():
    local_fruit = "Banana"
    print(f"Local fruit: {local_fruit}")
    print(f"Global fruit: {fruit_name}")

print_fruit()
print(f"Global fruit outside function: {fruit_name}")


# # 5. Recursion and Anonymous (Lambda) Function
# Recursion is a technique where a function calls itself. 
# 
# 
# This can be useful for solving problems that can be broken down into smaller,
# 
# 
# similar sub-problems.

# #Recursion with Fruits
# 
# 
# Recursion involves a function calling itself. In this example, 
# 
# 
# we'll use recursion to count the number of fruits in a basket.

# In[8]:


def count_fruits(basket):
    if not basket: 
    else:
        # Take out one fruit and call the function with the rest of the basket
        return 1 + count_fruits(basket[1:])

basket = ['apple', 'banana', 'orange', 'apple', 'kiwi']
num_fruits = count_fruits(basket)
print(f"There are {num_fruits} fruits in the basket.")

Anonymous (Lambda) Function with Fruits

Lambda functions are small, anonymous functions. In this example,

we'll use a lambda function to sort a list of fruits in alphabetical order.
# In[26]:


fruits = ['banana', 'apple', 'cherry', 'date']

sorted_fruits = sorted(fruits, key=lambda x: x.lower())
print(sorted_fruits)


# # 6. User Defined Functions
# These are the functions that you create to perform specific tasks in your code. 
# 
# All the examples above are examples of user-defined functions.

# In[7]:


def calculate_rectangle_area(length, width):
    area = length * width
    return area

# Input values
length = 8

width = 8

# Call the function and store the result
area_of_rectangle = calculate_rectangle_area(length, width)

# Print the result
print(f"The area of the rectangle with length {length} and width {width} is: {area_of_rectangle}")
          


# # Explanation:
# 
# Defining the Function:
# 
# We define a function called calculate_rectangle_area that takes two parameters: length and width.
# Performing the Calculation:
# 
# 
# Inside the function, we calculate the area by multiplying length with width.
# Returning the Result:
# 
# 
# We use return to send back the calculated area.
# Calling the Function:
# 
# 
# We call the function with specific values for length (5) and width (3).
# Storing the Result:
# 
# 
# The returned area is stored in the variable area_of_rectangle.
# Printing the Result:
# 
# 
# Finally, we print out the calculated area.

# In[2]:


a =  lambda x:"Even" if x%2 == 0 else 'odd'
a (85)


# In[1]:


list(map(lambda x:x**2,[1,2,3,4,5]))


# In[15]:


users = [
    {
        'name ': 'Anish',
        'age ' : 52,
        'gender ': 'male'
    },
    {
     'name ': 'Anisha',
        'age ': 25,
     'gender': 'Female'   
    },
    {
        
     'name ': 'Anamika',
        'age': 25,
        'gender': 'Female'
    }
]

list(map(lambda users: users.get('gender'), users))


# In[18]:


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
result = squared_numbers


# In[19]:


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
result = squared_numbers


# In[4]:


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
result = squared_numbers
print(result)


# In[23]:


numbers = [1, 2, 3, 4, 5]
squa_n = list(map(lambda x: x**2, numbers))
result = squa_n
print(result)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




