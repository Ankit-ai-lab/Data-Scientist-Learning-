#!/usr/bin/env python
# coding: utf-8

# # 9. String
# Defining a string
# 
# 
# Different ways to create string Accessing elements of the string 
# 
# 
# Escape sequence
# 
# 
# Raw string String methods 
# 
# 
# String formatting Expressions
1. Defining a String:
In Python, a string is a sequence of characters enclosed in either single (' ') 
or double (" ") quotes. Here's an example:
# In[2]:


my_string = 'Hello, World!'
print(type(my_string)) 


# In[3]:


a = 2.3
print(type(a))
print(a)


# In[1]:


# Different Ways to Create a String:
single_quoted = 'Hello'
double_quoted = "World"
multi_line = '''This is a
multi-line string.'''
print(single_quoted)
print(double_quoted)
print(multi_line)


# In[5]:


# Accessing Elements of the String:
my_string = "Hello, World!"
print(my_string[2])
print(my_string[-2])


# In[39]:


my_string = "Hello, World!"
#print(my_string[0])
#print(my_string[:-6])


# # Escape Sequence:

# In[4]:


# Escape Sequence:
escaped_string = "This is an escape sequence: \nNew line"
print(escaped_string)


# In[13]:


# Newline (\n)
message1 = "Hello\nWorld"
print(f"Newline (\n):\n{message1}\n")
# Explanation: The '\n' escape sequence inserts a newline character,
##creating a line break between "Hello" and "World".


# In[14]:


# Tab (\t)
message2 = "Hello\tWorld"
print(f"Tab (\t):\n{message2}\n")
# Explanation: The '\t' escape sequence inserts a tab character, adding space between "Hello" and "World".


# In[23]:


# Backslash (\\)
message3 = "This is a backslash: \\"
print(f"Backslash :\n{message3}\n")
# Explanation: To include a literal backslash in a string, you need to escape it with another backslash.


# In[16]:


# Single Quote (\')
message4 = 'Don\'t worry'
print(f"Single Quote (\'):\n{message4}\n")
# Explanation: To include a single quote within a single-quoted string, you need to escape it.


# In[17]:


# Double Quote (\")
message5 = "She said, \"Hello!\""
print(f"Double Quote (\"):\n{message5}\n")
# Explanation: To include a double quote within a double-quoted string, you need to escape it.


# In[18]:


# Carriage Return (\r)
message6 = "Hello\rWorld"
print(f"Carriage Return (\r):\n{message6}\n")
# Explanation: The '\r' escape sequence moves the cursor to the beginning of the line,
#effectively overwriting the previous text.


# In[19]:


# Backspace (\b)
message7 = "Hello\bWorld"
print(f"Backspace (\b):\n{message7}\n")
# Explanation: The '\b' escape sequence removes the preceding character (in this case, 'o').


# In[20]:


# Formfeed (\f)
message8 = "Hello\fWorld"
print(f"Formfeed (\f):\n{message8}\n")
# Explanation: The '\f' escape sequence advances the cursor to the next "page" or screen.


# In[21]:


# Vertical Tab (\v)
message9 = "Hello\vWorld"
print(f"Vertical Tab (\v):\n{message9}\n")
# Explanation: The '\v' escape sequence inserts a vertical tab character.


# In[22]:


# Bell (\a)
print("Beep!\a")
# Explanation: The '\a' escape sequence produces a bell or alert sound (usually a system-dependent sound).


# In[23]:


# Octal Value (\ooo)
message10 = "This is an octal value: \141"
print(f"Octal Value (\\ooo):\n{message10}\n")
# Explanation: The '\\ooo' escape sequence represents a character using its octal value. In this example, it represents the character 'a'.


# In[24]:


# Hexadecimal Value (\xhh)
message11 = "This is a hexadecimal value: \x41"
print(f"Hexadecimal Value (\\xhh):\n{message11}\n")
''' Explanation: The '\\xhh' escape sequence represents
a character using its hexadecimal value. In this example, it represents the character 'A'.
'''


# In[27]:


#     ------------------------------------       #


# # Raw String:

# In[5]:


# Raw String:
raw_string = r"This is a raw \n string"
print(raw_string)


# In[6]:


# String Methods:
my_string = "Hello, World!"
print(my_string.upper())
print(my_string.split(","))


# In[9]:


# Defining a String
my_string = "   hello, world!   "
print(f"Original String: '{my_string}'")

# Using String Methods
upper_case = my_string.upper()
lower_case = my_string.lower()


capitalized = my_string.capitalize()

title_case = my_string.title()

stripped = my_string.strip()

split_result = my_string.split(",")

joined = ', '.join(['hello', 'world'])

starts_with_hello = my_string.startswith("hello")

ends_with_world = my_string.endswith("world")

replaced = my_string.replace("world", "Python")

# Output
print(f"Uppercase: {upper_case}")
print(f"Lowercase: {lower_case}")
print(f"Capitalized: {capitalized}")
print(f"Title Case: {title_case}")
print(f"Stripped: '{stripped}'")
print(f"Split Result: {split_result}")
print(f"Joined: '{joined}'")
print(f"Starts with 'hello': {starts_with_hello}")
print(f"Ends with 'world': {ends_with_world}")
print(f"Replaced: '{replaced}'")


# In[7]:



# String Formatting:
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)


# In[1]:



# String Formatting:
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string) 


# In[8]:


# Expressions:
str1 = "Hello"
str2 = " World"
combined_str = str1 + str2
print(combined_str)


# # Formatted String (f-string):

# In[12]:


name = "Alice"
formatted_string = f"Hello, {name}!"
print(formatted_string)

'''
Explanation: An f-string allows you to embed expressions inside string literals,
using {} to indicate where the expression should be placed. 
In this example, the value of the variable name will be inserted into the string.
'''


# In[ ]:




