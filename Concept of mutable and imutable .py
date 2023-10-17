#!/usr/bin/env python
# coding: utf-8
n programming, mutable and immutable refer to whether an object's value can be changed after it has been created.

Mutable objects can be modified after creation, while immutable objects cannot be changed.

Here are some key points about mutable and immutable objects:

Immutable Objects:
Cannot be Changed: Once created, the value of an immutable object 
cannot be modified. Any attempt to modify the object will result in the creation of a new object.

Examples of Immutable Types:

#Integers (int)
#Floats (float)
#Strings (str)
#Tuples (tuple)
#Frozen sets (frozenset)
#Complex numbers (complex)
#Benefits of Immutability:

They are safer to use in multi-threaded environments where concurrent modification can lead to issues.
They can be used as dictionary keys because their value will not change.
Mutable Objects:
Can be Changed: Mutable objects allow for in-place modifications, meaning you
    can alter the object's value without creating a new object.

Examples of Mutable Types:

#Lists (list)
#Dictionaries (dict)
#Sets (set)
#Byte Arrays (bytearray)
#Benefits of Mutability:

They allow for more efficient operations when dealing with large datasets,
as you can modify the existing object rather than creating a new one.
# In[6]:


# Immutable Example (String)
name = "Alice"
new_name = name + " Smith"  # Creates a new string object
print(new_name)
print(name)      


# In[2]:


# Mutable Example (List)
numbers = [1, 2, 3]
numbers.append(4)  # Modifies the existing list
print(numbers) 


# In[1]:


# Mutable Example (List)
numbers = [1, 2, 3]
numbers.append(4)  # Modifies the existing list
print(numbers) 


# In[2]:


num = (1, 2, 3 , 4)
num.append(8)
prinnt(num)


# In[ ]:




