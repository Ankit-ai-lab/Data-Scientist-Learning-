#!/usr/bin/env python
# coding: utf-8

# # Problem: Write a Python program that evaluates a logical expression not (x or y) where x = True and y = False.

# In[1]:


x = True
y = False
result = not (x or y)
print(f"not (x or y) is {result}")


# # Problem: Write a Python program that checks if a given number is even or odd.

# In[2]:


num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# # Problem: Write a Python program that calculates the remainder when 15 is divided by 4.

# In[3]:


result = 15 % 4
print(f"The remainder is {result}")


# # Problem: Write a Python program that checks if x and y refer to the same object in memory.

# In[4]:


x = [1, 2, 3]
y = [1, 2, 3]
if x is y:
    print("x and y refer to the same object")
else:
    print("x and y refer to different objects")


# # Write a Python program that checks if the letter 'a' is present in the string "Hello, World!"

# In[5]:


string = "Hello, World!"
if 'a' in string:
    print("'a' is present in the string")
else:
    print("'a' is not present in the string")


# # Write a Python program that performs bitwise OR (|) operation on two binary numbers: 1010 and 1100

# In[6]:


num1 = 0b1010
num2 = 0b1100
result = num1 | num2
print(bin(result))


# In[7]:


# Write a Python program that evaluates a logical expression x and y where x = True and y = False.


# In[8]:


x = True
y = False
result = x and y
print(f"x and y is {result}")


# # Write a Python program that demonstrates the use of the assignment operators (+=, -=).

# In[9]:


x = 5
x += 3
y = 10
y -= 2
print(f"x: {x}, y: {y}")


# # Write a Python program that compares two numbers and prints whether the first number is greater,
# smaller, or equal to the second number.

# In[10]:


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num1} is equal to {num2}")


# # Write a Python program to perform addition and multiplication of two numbers entered by the user.

# In[11]:


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
addition = num1 + num2
multiplication = num1 * num2
print(f"Addition: {addition}, Multiplication: {multiplication}")


# In[ ]:




