#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib


# In[ ]:





# In[7]:


class A:
    """hello how are you"""    
    string_to_access = "Learn Coading AND Earn Money"
    age = 10

# Accessing the string
access_string = A.string_to_access
print(access_string)


# In[8]:


class A:
    age = 10
    name = "monu"
    def fun(self):
        "Ankit Amit Anush  "
        name = "Learn With Hum"
        print(name)
        
        "Ankit Amit Anush  "
        
obj = A()
obj.fun()
print(obj.fun.__doc__)
print(obj.age)
print(A.age) 
print(A.name)
#this is other way to aacces to the Class


# In[9]:


class A:
    
    def __init__(self ,age,name,ddress):  #constructor is majical method   (   __init__)
        print(age, " ",name," ",ddress)
        
obj=A (10,"Anit","mum")
obj = A(20,"Ramnagar",'rawan')


# In[1]:


class Atm:

  # constructor(special function)->superpower -> 
  def __init__(self):
    print(id(self))
    self.pin = ''
    self.balance = 0
    print("mai to excue ho gaya")
    #self.menu()

    def menu(self):
        user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[48]:


obj = Atm()


# In[60]:


class Atm:

  # constructor(special function)->superpower -> 
  def __init__(self):
    print(id(self))
    self.pin = ''
    self.balance = 0
   #print("mai to excue ho gaya")
    self.menu()

    def menu(self):
        user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)


# In[57]:


class Atm:

    def __init__(self):
        print(id(self))
        self.pin = ''
        self.balance = 0

    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)

obj = Atm()



# In[5]:


class Atm:

    def __init__(self):
        print(id(self))
        self.pin = ''
        self.balance = 0
        #self.menu()

    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input('enter your pin')
        self.pin = user_pin

        user_balance = int(input('enter balance'))
        self.balance = user_balance

        print('pin created successfully')
        self.menu()

    def change_pin(self):
        old_pin = input('enter old pin')

        if old_pin == self.pin:
            new_pin = input('enter new pin')
            self.pin = new_pin
            print('pin change successful')
            self.menu()
        else:
            print('nai karne de sakta re baba')
            self.menu()

    def check_balance(self):
        user_pin = input('enter your pin')
        if user_pin == self.pin:
            print('your balance is ', self.balance)
        else:
            print('chal nikal yahan se')

    def withdraw(self):
        user_pin = input('enter the pin')
        if user_pin == self.pin:
            # allow to withdraw
            amount = int(input('enter the amount'))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('withdrawal successful. Balance is', self.balance)
            else:
                print('abe garib')
        else:
            print('sale chor')
        self.menu()

obj = Atm()
obj.menu()


# In[3]:



class Temp:
   
   def __init__(self):
       print('hello')

#obj = Temp()


# In[4]:


print(Temp)


# In[ ]:




