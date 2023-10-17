#!/usr/bin/env python
# coding: utf-8

# # Tuples

# In[15]:


# empty
t1 = ()
print(t1)


# In[37]:


# create a tuple with a single item
t2 = ('hello',)
print(t2)
print(type(t2))


# In[35]:


num = '1, 2, 3'
print(type(num))


# In[33]:



anish = (1,2,3,4)
print(anish)


# In[22]:


t4 = (1,2.5,True,[1,2,3])
print(t4)


# In[23]:


# tuple
t5 = (1,2,3,(4,5))
print(t5)


# In[26]:


# using type conversion
t6 = tuple('hiii')
print(t6)


# In[27]:


# using type conversion
t6 = tuple('hiii')
print(t6)
print(type(t6))


# In[1]:


# empty
t1 = ()
print(t1)
# create a tuple with a single item
t2 = ('hello',)
print(t2)
print(type(t2))
# homo
t3 = (1,2,3,4)
print(t3)
# hetro
t4 = (1,2.5,True,[1,2,3])
print(t4)
# tuple
t5 = (1,2,3,(4,5))
print(t5)
# using type conversion
t6 = tuple('hiii')
print(t6)

Accessing Items
Indexing
Slicing
# In[3]:


print(t3)
print(t3[0])
print(t3[-1])


# In[7]:


# + and *
t1 = (1,2,3,4)
t2 = (5,6,7,8)

print(t1 + t2)

print(t1*3)
# membership
1 in t1
# iteration
for i in t1:
  print(i)


# # Operations on Tuples

# In[10]:


# Creating two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Arithmetic Operators
addition = tuple1 + tuple2  # Result: (1, 2, 3, 4, 5, 6)
multiplication = tuple1 * 2  # Result: (1, 2, 3, 1, 2, 3)

# Comparison Operators
equality = tuple1 == (1, 2, 3)  # Result: True
inequality = tuple1 != tuple2  # Result: True
greater_than = tuple2 > tuple1  # Result: True

# Membership Operators
contains = 2 in tuple1  # Result: True
not_contains = 4 not in tuple2  # Result: True

# Slice Operator
sliced = tuple1[1:3]  # Result: (2, 3)

# Comma Operator (Used to create a tuple)
comma_operator = 1, 2, 3  # Result: (1, 2, 3)

# Print the results
print("Addition:", addition)
print("Multiplication:", multiplication)
print("Equality:", equality)
print("Inequality:", inequality)
print("Greater Than:", greater_than)
print("Contains 2:", contains)
print("Doesn't Contain 4:", not_contains)
print("Sliced Tuple:", sliced)
print("Tuple created with comma operator:", comma_operator)


# In[52]:


# Arithmetic Operators
addition = tuple1 + tuple2  # Result: (1, 2, 3, 4, 5, 6)
multiplication = tuple1 *2 
print(multiplication)
print(addition)


# In[ ]:




Tuple Functions
# In[11]:


# len/sum/min/max/sorted
t = (1,2,3,4)
len(t)

sum(t)

min(t)

max(t)

sorted(t,reverse=True)


# In[12]:


# count

t = (1,2,3,4,5)

t.count(50)


# In[28]:


len(t)


# In[29]:


sum(t)


# In[53]:


max(t)


# In[41]:


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)


# In[45]:


# Membership Operators
contains = 4 not in tuple1  # Result: True
not_contains = 4 not in tuple2  # Result: True
print(contains)
print(not_contains)

