#!/usr/bin/env python
# coding: utf-8

# # Write a Python program that calculates the hypotenuse of a right triangle given the lengths of its two legs. Print the result.

# In[1]:


import math

def calculate_hypotenuse(leg1, leg2):
    hypotenuse = math.sqrt(leg1**2 + leg2**2)
    return hypotenuse

# Example usage
leg1 = 3
leg2 = 4
hypotenuse = calculate_hypotenuse(leg1, leg2)
print(f"The length of the hypotenuse is: {hypotenuse}")


# Write a Python program that adds two complex numbers (a + bi and c + di). Print the result.

# In[2]:


def add_complex_numbers(a, b, c, d):
    real_part = a + c
    imaginary_part = b + d
    return complex(real_part, imaginary_part)

# Example usage
a, b = 2, 3
c, d = 1, 4
result = add_complex_numbers(a, b, c, d)
print(f"The sum of complex numbers is: {result}")


# Write a Python program that converts a floating-point number to an integer. Print the result

# In[3]:


def convert_float_to_int(float_number):
    return int(float_number)

# Example usage
float_number = 5.7
result = convert_float_to_int(float_number)
print(f"The integer value is: {result}")


# Write a Python program that converts a string representing a binary number to its decimal equivalent. Print the result.

# In[4]:


def binary_to_decimal(binary_string):
    decimal_value = int(binary_string, 2)
    return decimal_value

# Example usage
binary_string = "101010"
result = binary_to_decimal(binary_string)
print(f"The decimal equivalent is: {result}")


# Write a Python program that generates a random integer between a specified range (inclusive). Print the result.

# In[5]:


import random

def generate_random_integer(min_range, max_range):
    return random.randint(min_range, max_range)

# Example usage
min_range = 10
max_range = 20
result = generate_random_integer(min_range, max_range)
print(f"The random integer is: {result}")


# Write a Python program that generates a random password of a specified length. The password should include a mix of uppercase letters, lowercase letters, and digits. Print the result.

# In[9]:


import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
password_length = 12
result = generate_random_password(password_length)
print(f"The random password is: {result}")


# Write a Python program that calculates the square root of a complex number (a + bi). Print the result.

# In[10]:


import cmath

def complex_square_root(a, b):
    complex_number = complex(a, b)
    sqrt_result = cmath.sqrt(complex_number)
    return sqrt_result

# Example usage
a, b = 5, 12
result = complex_square_root(a, b)
print(f"The square root of the complex number is: {result}")


# In[ ]:


Write a Python program that subtracts two complex numbers (a + bi and c + di). Print the result.


# In[11]:


def subtract_complex_numbers(a, b, c, d):
    real_part = a - c
    imaginary_part = b - d
    return complex(real_part, imaginary_part)

# Example usage
a, b = 2, 3
c, d = 1, 4
result = subtract_complex_numbers(a, b, c, d)
print(f"The difference of complex numbers is: {result}")


# In[14]:


#Write a Python program that generates a random word of a specified length using a combination of lowercase letters

word_length = 10

#The generated random word is: jhfweabnkt


# In[15]:


import random
import string

def generate_random_word(length):
    letters = string.ascii_lowercase
    random_word = ''.join(random.choice(letters) for _ in range(length))
    return random_word

# Example usage
word_length = 10
random_word = generate_random_word(word_length)
print(f"The generated random word is: {random_word}")


# # Write a Python program that generates a random name by combining a specified number of random syllables. Each syllable is constructed by randomly selecting a consonant followed by a vowel.

# In[16]:


import random

def generate_random_name(num_syllables):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    name = ''

    for _ in range(num_syllables):
        syllable = random.choice(consonants).capitalize() + random.choice(vowels)
        name += syllable

    return name

# Example usage
num_syllables = 2
random_name = generate_random_name(num_syllables)
print(f"The generated random name is: {random_name}")


# In[ ]:




