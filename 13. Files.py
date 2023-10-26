#!/usr/bin/env python
# coding: utf-8

# # Defining a File:
# A file is a collection of data stored on a computer. It could be a text file with words, a program file with code, or even an image or video file. In Python, you can work with files to read data from them or write data to them.
# 
# ##Types of File Operations:
# There are three main types of file operations:
# 
# Read ('r'): This allows you to open and read the contents of a file. You can't modify the file using this mode.
# 
# Write ('w'): This allows you to open and write to a file. If the file already exists, it will be overwritten. If not, a new file will be created.
# 
# Append ('a'): This allows you to open a file and add new content at the end. If the file doesn't exist, a new one will be created.
# 
# ##Opening a File:
# In Python, you can open a file using the open() function. It takes two arguments: the file path and the mode.

# In[17]:


file = open('sample.txt', 'r')  # Opens 'sample.txt' for reading
file.close


# In[ ]:





# # Closing a File:
# After you're done with a file, it's important to close it. This frees up system resources and ensures that any changes you made are saved.

# In[2]:


file.close()

File Modes:
File modes define the purpose of opening a file. Here are the three main modes:

'r': Read mode. Used for reading files.
'w': Write mode. Used for writing or creating new files.
'a': Append mode. Used for adding content to existing files.
# Writing to a File:
# In write mode ('w'), you can write data to a file. If the file already exists, it will be overwritten.

# # Using Context Manager (With)
# 
# 
# It's a good idea to close a file after usage as it will free up the resources
# 
# 
# If we dont close it, garbage collector would close it
# 
# 
# with keyword closes the file as soon as the usage is over

# In[3]:


with open('output.txt', 'w') as file:
    file.write("This is a line of text.")

    


# In[4]:


f.write('hello')


# In[12]:


# moving within a file -> 10 char then 10 char
with open('sample.txt','r') as f:
    print(f.read(10) )
    print(f.read(10))
    print(f.read(10))
    print(f.read(10))


# In[ ]:





# # Reading from a File:
# In read mode ('r'), you can read the contents of a file.

# In[14]:


with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)


# In[15]:


with open('output.txt', 'r') as file:
    content = file.read()
    print(content)
file.close()


# # Appending to a File:

# In[18]:


with open('sample.txt', 'a') as file:
    file.write("This is an additional line.")
file.close()

File Positions:
When you read from or write to a file, there's a "cursor" that keeps track of where you are. You can control this cursor using the seek() method.
# In[16]:


file.seek(0)


# # Binary Files:
# Binary files contain data that isn't in plain text format. They're used for things like images or executable programs. To work with binary files, use modes like 'rb' (read binary) or 'wb' (write binary).

# # Writing to a Binary File:

# In[23]:


# Create a binary file and write binary data to it
with open('binary_data.dat', 'wb') as file:
    data = bytes([65, 66, 67, 68, 69])  
    file.write(data)


# # Reading from a Binary File:

# In[24]:


# Read binary data from the file
with open('binary_data.dat', 'rb') as file:
    binary_data = file.read()

print(binary_data)


# # Writing Text Data ('w' or 'wr'):

# In[25]:


with open('text_data.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n")

Accessing a File Line by Line:
# In[26]:


with open('text_data.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character


# # Reading Binary Data ('rb')

# In[28]:


with open('binary_data.dat', 'rb') as file:
    binary_data = file.read()
    print(binary_data)


# In[29]:


binary_data = b'ABCDE'
text_data = binary_data.decode('utf-8')
print(text_data)


# In[ ]:





# In[31]:


# seek and tell function
with open('output.txt','r') as f:
    f.seek(15)
    print(f.read(10))
    print(f.tell())
    print(f.read(10))
    print(f.tell())


# In[ ]:





# # Pickle Module:
# The pickle module in Python is used for serializing and deserializing objects. This means you can save complex data structures (like lists or dictionaries) to a file and load them back later.
# 
# 

# In[33]:


import pickle

data = {'name': 'John', 'age': 30}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)


# In[ ]:




