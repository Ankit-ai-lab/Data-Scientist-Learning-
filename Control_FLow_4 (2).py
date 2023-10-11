#!/usr/bin/env python
# coding: utf-8

# ##4. Control Flow
# 
# • If statement
# 
# • If - else
# 
# 
# 
# • If – elif -else
# 
# • Nested if-else
# 
# 
# • while loop
# 
# • for – in loop
# 
# • Nested for loop
# 
# • Nester while loop
# 
# • Loop with else
# 
# • Pass statement
# 
# • Break and continue

# # If Statement:
# The if statement allows you to execute a block of code if a certain condition is true.
# 
# Example (Python):Suppose you want to check if a number x is positive:

# In[35]:


x = 5

if x >= 5:
    print("x is greter than 4")


# # 2. If - Else:
# Explanation:
# The if-else statement extends the if statement to include an action to perform when the condition is false.
# 
# Example:
# Let's modify the previous example to include an else statement:

# In[31]:


x = 3

if x > 2:
    print("x is positive")
else:
    
    print("x is not positive")


# # 3. If – Elif - Else:
# Explanation:
# The if-elif-else statement allows you to check multiple conditions in sequence.
# 
# Example:
# Let's say you want to classify a number x as positive, negative, or zero:

# In[42]:


x = 0

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")


# # 4. Nested if-else:
# Explanation:
# A nested if-else is an if-else statement inside another if or else block.
# 
# Example:
# Suppose you want to check if a number x is even or odd, and if it's even, you want to check if it's positive:

# In[ ]:





# In[37]:


fruit = input("Enter a fruit (apple, banana, or cherry): ")

if fruit == "apple":
    print("Apples are usually red or green  price is 25rs.")
elif fruit == "banana":
    print("Bananas are typically yellow when ripe.")
elif fruit == "cherry":
    color = input("Are the cherries red or black? ")
    if color == "red":
        print("Red cherries are sweet.")
    elif color == "black":
        print("Black cherries are tart.")
    else:
        print("Invalid color.")
else:
    print("This froot not available.") 


# In[6]:


train_direction = input("Enter train direction (western, herbal, central): ").lower()

if train_direction == "western":
    print("Welcome to the Western Line.")
elif train_direction == "herbal":
    
    print("Welcome to the Herbal Line.")
elif train_direction == "central":
    print("Welcome to the Central Line.")
else:
    print("Invalid train direction.")


# In[ ]:





# In[ ]:


### elif clause


# # 5. While Loop:
# Explanation:
# A while loop allows you to repeatedly execute a block of code as long as a condition is true.
# 
# Example:
# Let's say you want to print numbers from 1 to 5:

# In[43]:


#A = "hello , word"

#while A  10:
 #   print(A)
  #  A += 1
# 


# In[10]:


A = 1

while A <= 21:
    print(A)
    A += 1
 


# # 6. For – In Loop:
# Explanation:
# A for loop allows you to iterate over a sequence (like a list) and perform an action for each element.
# 
# Example:
# Suppose you want to print the elements of a list:

# In[17]:


fruits = ["apple", "banana", "cherry"]

for fruits in fruits :
    print(fruits)


# # Nested For Loop Example (Python):
# Explanation:
# A nested for loop is a loop inside another loop. In this example, 
# we'll use two loops to print out all possible combinations of fruits and colors.

# In[12]:


fruit = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "black"] 

for apple in fruit:
   for color in colors:
      print(f"The {fruit} is {color}")


# In[17]:


fruit = ["apple", "banana", "cherry","mango"]
colors = ["red", "yellow", "black","white"] 

for cherry in fruit:
   for color in colors:
      print(f"The {fruit} is {color}")


# # 8. Nested While Loop:
# Explanation:
# A nested while loop is a loop inside another loop.
# 
# Example:
# Suppose you want to print a pattern of stars:

# In[26]:


i = 2

while i <= 10:
    k = 1
    while k <= i:
        print("*", end="")
        k += 1 
    print()
    i += 1


# In[14]:


i = 1

while i <= 10:
    pratic = 1
    while pratic <= i:
        print("$", end =" ")
        pratic += 1
    print()
    i += 1


# In[ ]:





# In[ ]:





# In[ ]:





# # 9. Loop with Else:
# Explanation:
# In some languages, you can have an else block that executes if the loop completes without encountering a break statement.
# 
# Example:
# Let's say you want to find a prime number:

# In[9]:



i = 2

for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")


# # 10. Pass Statement:
# Explanation:
# The pass statement is a no-operation statement. It's used when a statement is syntactically required but you don't want any code to execute.
# 
# Example:
# Suppose you're working on an incomplete function:
# 
# 

# In[28]:


def my_function():
    pass


# # break:
# 
# When break is encountered in a loop, it immediately terminates the loop, and the program continues with the next statement after the loop.
# It's typically used to exit a loop early if a certain condition is met.

# In[29]:


students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

for student in students:
    if student == 'Bob':
        break
    print(f'hey  bro how are you, {student}!')


# # continue:
# 
# When continue is encountered, it skips the rest of the loop's code for the current iteration and continues with the next iteration.
# It's typically used to skip certain elements or operations within a loop based on a condition.

# In[22]:


students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

for student in students:
    if student == 'Charlie':
        print(f'Hello, {student}!')


# In[44]:


while True:
    #print("Hello, world!")           #continue loop
    


# # Questions:
# 1.Write a Python program that checks if a given number is even or odd. (Use if-else).
# 
# 2. Create a program that prints the first 10 multiples of 3. (Use a for loop).
# 
# 3. Write a program to find the sum of all numbers in a list. (Use a for loop).
#  

# In[ ]:




