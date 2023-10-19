#!/usr/bin/env python
# coding: utf-8

# # Typecasting:
# 
# Typecasting involves converting a value from one data type to another. 
# For example, converting an integer to a floating-point number.

# In[1]:


# Typecasting examples
x = 10.5
y = int(x)   # Convert float to integer, y will be 10

a = 5
b = float(a)  # Convert integer to float, b will be 5.0


# # Numeric Functions:
# 
# These are functions that operate on numeric values. Examples include addition, subtraction, multiplication, division, 
# and more advanced operations like exponentiation, square root, etc.

# In[2]:


# Numeric functions
import math

# Square root
sqrt_val = math.sqrt(25)  # sqrt_val will be 5.0

# Exponentiation
exp_val = math.exp(2)     # exp_val will be e^2 or roughly 7.389

# Absolute value
abs_val = abs(-10)        # abs_val will be 10


# In[6]:


# Integer
x = 5

# Floating-point
y = 2.5

print(f"x = {x}")
print(f"y = {y}")


# In[7]:


# Addition, Subtraction, Multiplication, and Division
sum_result = 5 + 3  # sum_result will be 8
difference = 10 - 4  # difference will be 6
product = 7 * 2  # product will be 14
quotient = 15 / 3  # quotient will be 5.0


# In[8]:


print(sum_result)


# # Random Number Generation:

# In[5]:


import random

# Generate a random integer between 1 and 10
random_int = random.randint(1, 10)

# Generate a random floating-point number between 0 and 1
random_float = random.random()

print(f"Random Integer: {random_int}")
print(f"Random Float: {random_float}")


# In[ ]:




