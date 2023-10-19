#!/usr/bin/env python
# coding: utf-8

# # Sets
# A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# 
# 
# However, a set itself is mutable. We can add or remove items from it.
# 
# 
# Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.
# 
# 
# Characterstics:
# 
# 
# Unordered
# 
# 
# Mutable
# 
# 
# No Duplicates
# 
# 
# Can't contain mutable data types
 Set 
Defining a set 
Creating set 
Set operations 
Set methods
Set comprehension
# # Creating Set

# In[1]:


# empty 
# empty
s = set()
print(s)
print(type(s))


# In[2]:


# 1D and 2D
s1 = {1,2,3}
print(s1)


# In[14]:


# using type conversion

s4 = set([1,2,3,3,4])
print(s4)


# In[7]:


ss = set ([1,5])
print(type(ss))


# In[12]:


# duplicates not allowed
s5 = {1,8,2,2}
print(s5)


# In[15]:


# Creating a set
my_set = {1, 2, 3, 4, 5}


# In[ ]:





# In[ ]:





# In[ ]:





# In[18]:


my_set.add(5)
print(my_set)


# a set itself is mutable. We can add or remove items from it.

# In[21]:


my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Adding a new element
my_set.add(6)
print("Set after adding 6:", my_set)


# In[22]:


#Removing Elements from a Set:


# In[24]:


my_set2 = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Removing an element
my_set2.remove(3)
print("Set after removing 3:", my_set)


# # set opperations
# Union
# 
# Intersection
# 
# Difference
# 
# Symmetric Difference

# # set opperations
# ##1. Union
# The union of two sets contains all unique elements from both sets.

# In[26]:


set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)


# # 2. Intersection
# The intersection of two sets contains only the elements that exist in both sets.

# In[27]:


set1 = {1, 2, 3}
set2 = {3, 4, 5}

intersection_set = set1.intersection(set2)
print(intersection_set)


# # 3. Difference
# The difference between two sets contains elements present in the first set but not in the second.

# In[28]:


set1 = {1, 2, 3}
set2 = {3, 4, 5}

difference_set = set1.difference(set2)
print(difference_set)


# # 4. Symmetric Difference
# The symmetric difference contains elements that are in either of the sets, but not in their intersection

# In[29]:


set1 = {1, 2, 3}
set2 = {3, 4, 5}

symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)


# In[ ]:





# # Set Method
# add(): Adds an element to the set.

remove(): Removes a specified element from the set. Raises an error if the element does not exist.

discard(): Removes a specified element from the set. Does not raise an error if the element does not exist.

clear(): Removes all elements from the set.

copy(): Returns a shallow copy of the set.

pop(): Removes and returns an arbitrary element from the set. Raises an error if the set is empty.

difference(): Returns a new set with elements in the set but not in the specified set(s).

intersection(): Returns a new set with elements common to the set and the specified set(s).

union(): Returns a new set containing all elements from the set and the specified set(s).

issubset(): Returns True if all elements of a set are present in another set.
# In[35]:


#s = {1,2,5,3}
s = {2}
s.pop()
print(s)


# In[36]:


s = {1,2,5,3}

s.add(2)
print(s)


# In[37]:


r = {22,22,5,6}
r.remove(22)


# In[38]:


print(r)


# # Set Comprehension
# Set comprehension is a concise way to create a set using a single line of code.

# In[19]:


squares = {x**2 for x in range(1, 6)}
print(squares) 


# In[39]:


{i**2 for i in range(1,11) if i>5}


# # set function

# In[41]:


# len/sum/min/max/sorted
s = {3,1,4,5,2,7}
len(s)
sum(s)
min(s)
max(s)
sorted(s,reverse=True) 


# In[42]:


sum(s)


# In[44]:


my_set = {1, 2, 3, 4, 5}

# Delete the set
del my_set


# In[47]:


se = {1,1,55,2}
print(se)



# In[48]:


del se


# In[49]:


print(se)


# In[ ]:




