#!/usr/bin/env python
# coding: utf-8

# Write a Python function named greet that prints "Hello, World!" when called.

# In[1]:


def greet():
    print("Hello, World!")


# In[2]:


greet()


# # Write a Python function named calculate_total_cost that takes three parameters: items (a list of item prices) #discount_percent, and tax_percent. The function should calculate the total cost after applying the discount #and taxes, and then return the result.

# In[4]:


items = [50, 30, 20, 10]  # Prices of items in the cart
discount_percent = 10    # 10% discount
tax_percent = 8          # 8% tax


# In[3]:


def calculate_total_cost(items, discount_percent, tax_percent):
    subtotal = sum(items)
    discount_amount = (discount_percent / 100) * subtotal
    discounted_total = subtotal - discount_amount
    tax_amount = (tax_percent / 100) * discounted_total
    total_cost = discounted_total + tax_amount
    return total_cost

# Example usage
items = [50, 30, 20, 10]
discount_percent = 10
tax_percent = 8

total_cost = calculate_total_cost(items, discount_percent, tax_percent)
print(f"The total cost after discounts and taxes is: ${total_cost:.2f}")


# Define a function named add_numbers that takes two parameters x and y and returns their sum.

# In[ ]:


def add_numbers(x, y):
    return x + y


# Use the add_numbers function to calculate the sum of 5 and 7.

# In[ ]:


result = add_numbers(5, 7)
print(result)


# Write a function named find_max that takes a list of numbers as a parameter and returns the maximum value.

# In[11]:


def find_max(numbers):
    return max(numbers)

# Example usage
numbers = [3, 8, 1, 6, 2, 7, 9, 4, 5]
max_number = find_max(numbers)
print(f"The maximum number in the list is: {max_number}")


# Write a Python program that demonstrates call by value and call by reference using lists.

# In[8]:


def modify_list(my_list):
    my_list.append(4)

num_list = [1, 2, 3]
modify_list(num_list)
print(num_list)  # Output: [1, 2, 3, 4]


# Write a Python program that demonstrates the use of local and global variables.

# In[10]:


global_var = "I am a global variable"

def my_function():
    local_var = "I am a local variable"
    print(global_var)
    print(local_var)

my_function()
print(global_var)
print(local_var)  # This will raise an error since local_var is not accessible here.


# Write a recursive function to calculate the factorial of a non-negative integer.

# In[13]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
result = factorial(5)
print(f"The factorial of 5 is: {result}")


# Define a lambda function that calculates the square of a number.

# In[14]:


square = lambda x: x**2
print(square)


# Write a Python program that defines a user-defined function and demonstrates its usage.

# In[15]:


def my_function(x):
    return x + 5

result = my_function(3)
print(result)  # Output: 8


#  Define a function named is_prime that takes an integer as input and returns True if it's a prime number, otherwise False.

# In[17]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
test_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for num in test_numbers:
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")


# # Find Duplicates:

# In[23]:


def find_duplicates(elements):
    return [item for item in set(elements) if elements.count(item) > 1]

# Example usage
test_elements = [1, 2, 3, 2, 4, 5, 3, 6, 2, 7, 7, 8]
duplicates = find_duplicates(test_elements)
print(f"The duplicates in the list are: {duplicates}")


# In[ ]:





# In[ ]:




