#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Defining a Dictionary
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Creating a Dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}


# # Accessing items

# In[10]:


# empty dictionary
d = {}
d
# 1D dictionary
d1 = { 'name' : 'nitish' ,'gender' : 'male' }
d1
# with mixed keys
d2 = {(1,2,3):1,'hello':'world'}
d2
# 2D dictionary -> JSON
s = {
    'name':'nitish',
     'college':'bit',
     'sem':4,
     'subjects':{
         'dsa':50,
         'maths':67,
         'english':34
     }
}
s
# using sequence and dict function
d4 = dict([('name','nitish'),('age',32),(3,3)])
d4
# duplicate keys
d5 = {'name':'nitish','name':'rahul'}
d5
# mutable items as keys
d6 = {'name':'nitish',(1,2,3):2}
print(d6)


# In[14]:


my_dict = {'name': 'Jack', 'age': 26}
# []
my_dict['age']
print(my_dict)
# get
my_dict.get('age')

s['subjects']['dsa']


# # Adding key-value pair

# In[15]:


d4


# In[12]:


d4['gender'] = 'male'
d4
d4['weight'] = 72
d4

s['subjects']['ds'] = 75
s


# # all method

# In[3]:


# Dictionary Methods

# 1. clear()
# Removes all items from the dictionary.

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict.clear()
print(my_dict)  # Output: {}

# 2. copy()
# Creates a shallow copy of the dictionary.

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# 3. items()
# Returns a view of the dictionary's key-value pairs.

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# 4. keys()
# Returns a view of the dictionary's keys.

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

# 5. values()
# Returns a view of the dictionary's values.

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.values())  # Output: dict_values(['John', 30, 'New York'])

# 6. get(key[, default])
# Returns the value for the specified key. 
# If the key does not exist, it returns the default value (which is None if not provided).

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.get('name'))  # Output: John
print(my_dict.get('address'))  # Output: None
print(my_dict.get('address', 'Not Found'))  # Output: Not Found

# 7. pop(key[, default])
# Removes the item with the specified key and returns its value. 
# If the key does not exist, it returns the default value (or raises a KeyError if not provided).

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.pop('age'))  # Output: 30
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}

# 8. popitem()
# Removes and returns an arbitrary key-value pair from the dictionary.

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
item = my_dict.popitem()
print(item)  # Output: ('city', 'New York')
print(my_dict)  # Output: {'name': 'John', 'age': 30}


# In[18]:


my_dict = {'name': 'John', 'city': 'New York','age': 30}
item = my_dict.popitem()
print(item)  # Output: ('city', 'New York')
print(my_dict)  


# In[16]:


my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.get('name'))  # Output: John
print(my_dict.get('address'))  # Output: None
print(my_dict.get('address', 'Not Found')) 


# # Problem: Create a dictionary with numbers as keys and their squares as values.

# In[2]:


squares = {}
for num in range(1, 6):
    squares[num] = num ** 2
print(squares)

Using Dictionary Comprehension:
# In[4]:


squares = {num: num**2 for num in range(1, 6)}
print(squares)


# In[6]:


squres = {}
for num in range (1,6):
    squares[num] = num**2
    squares = {num : num**2 for num in range (1, 6 )}
    print(squares)


# In[ ]:


#


# In[20]:


# print 1st 10 numbers and their squares
#{i:i**1 for i in range(1,11)}

distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
print(distances.items())


# In[6]:



# using existing dict
distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
{key:value*0.62 for (key,value) in distances.items()}


# In[5]:


# using zip
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

{i:j for (i,j) in zip(days,temp_C)}


# In[7]:



# using if condition
products = {'phone':10,'laptop':0,'charger':32,'tablet':0}

{key:value for (key,value) in products.items() if value>0}


# In[ ]:





# In[8]:







# Nested Comprehension
# print tables of number from 2 to 4
{i:{j:i*j for j in range(1,11)} for i in range(2,5)}

{
    2:{1:2,2:4,3:6,4:8},
    3:{1:3,2:6,3:9,4:12},
    4:{1:4,2:8,3:12,4:16}
}


# In[ ]:




