#!/usr/bin/env python
# coding: utf-8

# Write a Python program that creates a new text file named sample.txt and writes the following lines to the file:
#     Hello, World!
# This is a sample file.
# 

# In[1]:


# Create a new file and write to it
with open('sample.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")

print("File 'sample.txt' created and written successfully.")


# Write a Python program that reads the content of the file sample.txt and prints it to the console.

# In[ ]:


# Read from the file
with open('sample.txt', 'r') as file:
    content = file.read()

print(content)


# Write a Python program that appends the following line to the file sample.txt:
#     
#     Appending a line to the file.
# 

# In[2]:


# Append a line to the file
with open('sample.txt', 'a') as file:
    file.write("Appending a line to the file.\n")

print("Line appended to 'sample.txt'.")


# Write a Python program that reads the first two lines from the file sample.txt and prints them to the console.

# In[5]:


# Read first two lines from the file
with open('sample.txt', 'r') as file:
    lines = file.readlines()

print(lines[:2])


# Write a Python program that creates a binary file named binary_data.dat and writes a sequence of 10 integers to the file.

# In[6]:


# Create a binary file and write to it
with open('binary_data.dat', 'wb') as file:
    for i in range(10):
        file.write(i.to_bytes(4, byteorder='big'))

print("Binary file 'binary_data.dat' created and written successfully.")


# In[ ]:





# In[ ]:





# In[ ]:




