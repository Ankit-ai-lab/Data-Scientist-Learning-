#!/usr/bin/env python
# coding: utf-8
10. List
• Defining a list
• Creating list
• Accessing list elements of list
• Deleting list
• List methods
• Functions used with list
• List comprehension
• Implementation of stack and queue using list
• Use of Zip ()
• Matrix operations using list
# In[12]:


# Defining a list
fruits = ['apple', 'banana', 'cherry', 'date']


# In[13]:


# List with different data types
mixed_list = [1, 'apple', 3.14, True]
print (mixed_list)


# In[ ]:




Accessing List Elements:

#We demonstrate various methods to access elements:
#Using Indexing: Accessing elements by their position in the list (starting from index 0).
#Negative Indexing: Accessing elements from the end of the list.
#Slicing: Creating a new list from a portion of an existing list.
#Extended Slicing: Specifying a step size in addition to start and end indices.
#Looping through List: Using a loop to iterate through all elements of a list.
#Using 'in' Operator: Checking if an item is present in the list.
#List Comprehension: Creating a new list based on conditions applied to the elements of an existing list.
#Using index() Method: Finding the index of the first occurrence of a specified element.
# In[14]:


# Creating a List
fruits = ['apple', 'banana', 'cherry', 'date']


# # Accessing List Elements

# In[15]:


# Accessing List Elements

# Using Indexing
print(fruits[0])  # Output: 'apple'
print(fruits[2]) 


# In[16]:


# Negative Indexing
print(fruits[-1])  # Output: 'date'
print(fruits[-2]) 


# In[40]:


# Slicing
numbers = [1, 2, 3, 4,88, 5]
print(numbers[1:4])  # Output: [2, 3, 4]


# In[54]:


# Extended Slicing
print(numbers[1:5:2]) 


# In[38]:


# Looping through List
fruits = ['anaa', 'mango', 'buffer','banana']
for fruit in fruits:
    print(fruit)


# In[37]:


# Using 'in' Operator
#print('book' in fruits)


# In[41]:


# List Comprehension
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)


# In[42]:


# Using index() Method
print(fruits.index('buffer')) 

Method 1: Using the del Statement:

The del statement is used to remove the entire list.
Method 2: Clearing the List with clear():

The clear() method removes all elements from the list, effectively making it an empty list.
Method 3: Removing Specific Elements with remove():

The remove() method is used to remove the first occurrence of a specified element from the list.
Method 4: Using Slicing to Remove Elements:

Slicing can be used to remove specific elements or even a range of elements from the list.
Method 5: Using Pop:

The pop() method is used to remove and return an element at a specified index.
Method 6: Using List Comprehension:

List comprehension can be used to create a new list excluding specific elements.
# In[57]:



# Method 1: Using the del Statement
fruits = ['apple', 'banana', 'cherry', 'date']
del fruits
print(fruits)


# In[26]:


# Deleting Elements and Lists

# Method 1: Using the del Statement
fruits = ['apple', 'banana', 'cherry', 'date']
del fruits
# print(fruits)  # Error: NameError: name 'fruits' is not defined

# Method 2: Clearing the List with clear()
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # Output: []

# Method 3: Removing Specific Elements with remove()
fruits = ['apple', 'banana', 'cherry', 'date', 'banana']
fruits.remove('banana')  # Removes the first occurrence of 'banana'
print(fruits)  # Output: ['apple', 'cherry', 'date', 'banana']

# Method 4: Using Slicing to Remove Elements
numbers = [1, 2, 3, 4, 5]
numbers = numbers[:2] + numbers[3:]
print(numbers)  # Output: [1, 2, 4, 5]

# Method 5: Using Pop
numbers = [1, 2, 3, 4, 5]
removed_element = numbers.pop(2)  # Removes element at index 2 (3)
print(removed_element)  # Output: 3
print(numbers)  # Output: [1, 2, 4, 5]

# Method 6: Using List Comprehension
numbers = [1, 2, 3, 4, 5]
numbers = [x for x in numbers if x != 3]
print(numbers)  # Output: [1, 2, 4]


# In[46]:


# Method 3: Removing Specific Elements with remove()
fruits = ['apple', 'banana', 'cherry', 'date', 'banaana']
fruits.remove('banana')  # Removes the first occurrence of 'banana'
print(fruits)  


# # function use with list

# In[48]:


# len(): Returns the length of the list
numbers = [1, 2, 3, 4, 5]
list_length = len(numbers)  # Output: 5
print("Length of the list:", list_length)


# In[49]:


# max(): Returns the maximum value in the list
max_value = max(numbers)  # Output: 5
print("Maximum value in the list:", max_value)


# In[ ]:





# In[ ]:





# In[50]:


# Functions Used with Lists

# len(): Returns the length of the list
numbers = [1, 2, 3, 4, 5]
list_length = len(numbers)  # Output: 5
print("Length of the list:", list_length)

# max(): Returns the maximum value in the list
max_value = max(numbers)  # Output: 5
print("Maximum value in the list:", max_value)

# min(): Returns the minimum value in the list
min_value = min(numbers)  # Output: 1
print("Minimum value in the list:", min_value)

# sum(): Returns the sum of all elements in the list
total_sum = sum(numbers)  # Output: 15
print("Sum of all elements in the list:", total_sum)

# sorted(): Returns a sorted version of the list without modifying the original list
sorted_numbers = sorted(numbers)  # Output: [1, 2, 3, 4, 5]
print("Sorted list:", sorted_numbers)

# reversed(): Returns an iterator that iterates over the elements of the list in reverse order
reverse_iterator = reversed(numbers)
reversed_list = list(reverse_iterator)
print("Reversed list:", reversed_list)

# zip(): Combines multiple lists element-wise, creating a list of tuples
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]
name_age_pairs = list(zip(names, ages))  # Output: [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
print("Zipped list of names and ages:", name_age_pairs)

# enumerate(): Returns an enumerate object, which contains pairs of index and element
for index, value in enumerate(numbers):
    print(f"Element at index {index} is {value}")

# any(): Returns True if at least one element in the list is True (or evaluates to True)
bool_list = [True, False, False]
any_true = any(bool_list)  # Output: True
print("At least one element is True:", any_true)

# all(): Returns True if all elements in the list are True (or evaluate to True)
all_true = all(bool_list)  # Output: False
print("All elements are True:", all_true)


# In[51]:


# List Comprehensions

# Example 1: Creating a list of squares
squares = [x**2 for x in range(1, 6)]
print("List of squares:", squares)  # Output: [1, 4, 9, 16, 25]

# Example 2: Filtering odd numbers
odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
print("List of odd numbers:", odd_numbers)  # Output: [1, 3, 5, 7, 9]

# Example 3: Creating a list of tuples
names = ['Alice', 'Bob', 'Charlie']
name_length_pairs = [(name, len(name)) for name in names]
print("List of name-length pairs:", name_length_pairs)  # Output: [('Alice', 5), ('Bob', 3), ('Charlie', 7)]

# Example 4: Flattening a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [num for row in matrix for num in row]
print("Flattened matrix:", flattened_matrix)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 5: Generating a list of even numbers using conditional expression
even_numbers = [x if x % 2 == 0 else 'Odd' for x in range(1, 11)]
print("List of even numbers (with 'Odd' for odd numbers):", even_numbers)
# Output: ['Odd', 2, 'Odd', 4, 'Odd', 6, 'Odd', 8, 'Odd', 10]


# # 9

# In[52]:


# Stack Implementation using a List

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

# Example usage:
stack = Stack()
stack.push("Apple")
stack.push("Banana")
stack.push("Cherry")

print(stack.items)  # Output: ['Apple', 'Banana', 'Cherry']

popped_fruit = stack.pop()
print("Popped fruit:", popped_fruit)  # Output: Cherry
print("Stack after popping fruit:", stack.items)  # Output: ['Apple', 'Banana']

top_fruit = stack.peek()
print("Top fruit:", top_fruit)  # Output: Banana

Stack is like a stack of books. You can add a book on top (push),
take the top book off (pop), and see which book is on top (peek).
# In[ ]:





# In[53]:


# Queue Implementation using a List

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

# Example usage:
queue = Queue()
queue.enqueue("Apple")
queue.enqueue("Banana")
queue.enqueue("Cherry")

print(queue.items)  # Output: ['Apple', 'Banana', 'Cherry']

dequeued_fruit = queue.dequeue()
print("Dequeued fruit:", dequeued_fruit)  # Output: Apple
print("Queue after dequeueing fruit:", queue.items)  # Output: ['Banana', 'Cherry']

imple Explanation:

A Queue is like waiting in a line. You can join the line at the back (enqueue), and the person at the
front gets served first (dequeue).
These implementations use lists (self.items) to hold the elements. The methods (push, pop, peek for stack,
and enqueue, dequeue for queue) allow you to perform operations on the data structure. 
The is_empty method checks if the data structure is empty.
# In[ ]:





# In[ ]:




