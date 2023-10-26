#!/usr/bin/env python
# coding: utf-8

# Write a Python program to generate a multiplication table (up to 10) using nested for loops.

# In[1]:


for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()


#  Create a program that calculates the sum of all numbers from 1 to 10 using a for loop.

# In[2]:


total = 0
for num in range(1, 11):
    total += num
print(f"The sum is {total}")


# Write a Python program to print even numbers between 1 and 10 using a for loop.

# In[3]:


for num in range(2, 11, 2):
    print(num)


#  Create a program that calculates the factorial of a given number using a while loop.

# In[4]:


num = int(input("Enter a number: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(f"The factorial is {factorial}")


# Write a Python program to print numbers from 1 to 5 using a while loop.

# In[5]:


num = 1
while num <= 5:
    print(num)
    num += 1


#  Create a program that determines if a given number is positive, negative, or zero using nested if-else statements.

# In[6]:


num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")


#  Write a Python program to determine if a given year is a leap year using nested if-else statements.

# In[7]:


year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")


# Create a program that determines the grade (A, B, C, D, or F) for a given percentage using if-elif-else statements.

# In[8]:


percentage = float(input("Enter the percentage: "))
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# Write a Python program to classify a given angle (in degrees) as acute, obtuse, or right using if-elif-else statements.

# In[9]:


angle = float(input("Enter the angle in degrees: "))
if angle < 90:
    print("Acute angle.")
elif angle == 90:
    print("Right angle.")
else:
    print("Obtuse angle.")


#  Create a program that checks if a user-provided password matches a predefined correct password using an if-else statement.

# In[ ]:





# In[10]:


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# In[ ]:





# ###Write a program that takes a user's age and determines if they are eligible to vote using an if statement.

# In[11]:


age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# # Write a Python program to check if a given number is positive using an if statement.

# In[12]:


num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")


# In[ ]:




