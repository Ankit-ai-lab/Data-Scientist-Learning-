#!/usr/bin/env python
# coding: utf-8
3. Basics of Python
• Variable
• Keywords
• Statements & Comments
• Indentation
• Data types

• Input and outputVariables:

Variables are used to store data in a program.
They can hold different types of data such as numbers, strings, lists, etc.
# In[24]:



#input("enter your name ")
print("my name is 10")


# In[25]:


name = "jonh"
age = 30 


# In[26]:


name = 
print(type(name))   #print functio is givng output 


# In[31]:


# Define some variables
name = "Alice"


age = 30

pi = 3.14

is_active = True
numbers = [1, 2, 3]
coordinates = (10, 20)
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# Check data types
print(type(name))         # Output: <class 'str'>
print(type(age))           # Output: <class 'int'>
print(type(pi))           # Output: <class 'float'>
print(type(is_active))    # Output: <class 'bool'>
print(type(numbers))      # Output: <class 'list'>
print(type(coordinates))  # Output: <class 'tuple'>
print(type(person))       # Output: <class 'dict'>


# In[28]:


a = input("enter your name  ")
print(a,"hello")

Keywords:

Keywords are reserved words that have a specific meaning in Python.
Examples: if, else, for, while, def, class, etc.
Statements & Comments:

Statements are individual lines of code that perform an action.
Comments are used to explain code and are not executed by the interpreter.
Example:
# In[12]:


import keyword

# Get the list of reserved keywords
keywords = keyword.kwlist

# Print the list of keywords
print(keywords)


# In[4]:


# This is a comment
print("Hello, World!")  # This is also a comment

Indentation:
  
Python uses indentation (whitespace) to define blocks of code. This is different from languages like C++ or Java which use braces {}.
Example:
# In[13]:


x = 6
    

if x > 5:     # '''    '''
    print ("x is than 5")

Static Typing vs Dynamic Typing:

Python is dynamically typed, which means you don't have to specify the type of a variable when you declare it. The type is inferred at runtime.
Example:
# In[6]:


x = 5       # x is an integer
x = "Hello" # x is now a string


# In[9]:


##Input and Output:
 
input() #is used to take input from the user.
print() #is used to display output to the console.


# In[19]:


print("shhhh")


# In[4]:


input("enter your name  ")


# # Type Casting
# Similar to type conversion, type casting is done when we want to specify a type on a variable.

# In[8]:


A = 5
print(bool(A))


# In[9]:


print(type(A))  # Output: <class 'int'>


# In[10]:


str1 = "7"          
str2 = "3.142"
str3 = "13"
num1 = 29
num2 = 6.67

print(int(str1))
print(type(str1))
print(float(str2))
print(float(str3))
print(str(num1))
print(str(num2))


# In[13]:


str3 = "13"
print(float(str3))
print(type(str3))


# In[14]:


# Convert an integer to a string
my_integer = 42
my_string = str(my_integer)

# Check the type of my_string
print(type(my_string))  # Output: <class 'str'>

  


# In[31]:


a = {"ankit": 25}
print(type(a))


# In[30]:


bank = "88"
my_bank_int = bool(bank)
print(type(my_bank_int))


# In[19]:


bank = "88"
print(type(bank))
my_bank_int = int(bank)
print(type(my_bank_int))


# In[36]:


bank = "123"
my_bank_int = list(bank)
print(type(my_bank_int))  # This will print <class 'int'>
print(type(bank))


# In[38]:


bank = "123"
my_bank_int = list(bank)
print(type(my_bank_int))  # This will print <class 'int'>
print(type(bank))


# In[29]:


# a = int(input("enter your age") 
#         print(a)


# In[30]:



a = ["anil"]
print(type(a))


# In[ ]:




