#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = int(input())
b = int(input())
print(a/b)


# In[52]:



try:
    
    a = int(input())
    b = int(input())
    print(a/b)
    
except Exception as e:
    print("KUCH TOH GADBAD HAI...")
    print(e.args)
    print("Please give non -zero elements.")

else :
    print("This will execute if try block executes")

finally:
    print("THis is always run..")


# In[55]:


## main()
def main():
    # Code to be executed
    print("Hello, 10world!")

# Call the main function to start the program
main()


# In[7]:


def main():
    n1 = float(input())
    n2 = float(input())

    print(n1/n2)


# In[56]:


try:
    main()
    print(j)

except ZeroDivisionError as e:
    print("zero se division nahi hota, gadhe")
    print(e.args)
    main()

except ValueError as e :
    print(e.args)
    print(e.with_traceback)
    main()
    
except Exception as e:
    print("GEneral error")
    print(e.args)


# In[60]:


try:
    n1 = float(input())
    n2 = float(input())

    print(n1/n2)
    
except ZeroDivisionError as e:
    print(e.args)
    

except Exception as e:
    print(e.args)
    print("kuch toh gadbad hai...")
    
    

print("SOME STATEMENTS")


# In[15]:


5/0


# In[2]:


print(c)


# In[3]:


for i in "FKSKF"


# In[4]:


int("FHSDK")


# In[ ]:


n


# # EXCEPTIONS :
# - Exceptions are events that disrupt the normal flow of a program's execution when an error or unexpected situation occurs. 
# - These errors can range from simple issues like dividing by zero or trying to access a non-existent variable to more complex  problems like attempting to open a file that doesn't exist.
# - Exceptions in Python are objects that encapsulate information about the error, including the error type and, often, additional details about what caused the error.
# 
# # Exception Handling : 
# - Exception handling refers to the process of managing and responding to exceptions in a way that allows a program to gracefully handle errors without crashing. 
# ---
# - **Python provides a structured way to perform exception handling using the `try`, `except`, `else`, and `finally` blocks.**
# 
#     - `try:` This block contains the code that might raise an exception. It's the segment where exceptions are monitored.
# 
#     - `except:` This block follows the try block and specifies what should happen if an exception occurs. You can have multiple except blocks to handle different types of exceptions.
# 
#     - `else:` This block is executed if no exceptions occur in the try block. It's used to execute code that should run only when there are no exceptions.
# 
#     - `finally:` This block is always executed, whether an exception occurred or not. It's used for cleanup tasks or actions that should occur regardless of exceptions.
#     
# ---

# In[ ]:


try:
    # code that may throw error
except Exception as e:
    # code to handle the error
else:
    # code that will run only if try block runs without throwing an error
finally:
    # this code will always run.
    


# In[63]:


try:
    x = float(input("Enter a number : "))                # This will raise a ZeroDivisionError
    y = float(input("Enter a number : "))
    
    print(x/y)
        
except ZeroDivisionError as e:
    print(f"Error: {e}")
    
except ValueError as e:
    print(f"error: {e}")
    
except NameError as e:
    print("Kuch toh define nahi hai", e.args)
    
except Exception as e:
    print("KUCH TOH GADBAD HAI....")
    
else:
    print("No exception occurred.")
    
finally:
    print("This will always execute.")


# In[65]:


try:
    file = open("abc.txt",'r')
    
except Exception as e:
    print("file not present, creating new file.")
    file= open('abc.txt','w')
    file.write("Something")
    
else :
    print(file.read())
    
finally:
    file.close()


# In[ ]:


try:
    file = open("sample.txt", "w")
    file.write("Hello, world!")
except IOError as e:
    print(f"IO Error: {e}")
finally:
    file.close()


# # Custom Errors.
# - *User-defined errors*, also known as *custom exceptions*, allow you to create your own exception classes in Python. 
# - This can be useful when you want to handle specific error conditions in a more structured and meaningful way. 
# - To create a custom exception, you typically define a new class that inherits from the built-in `Exception` class or one of its subclasses. 
# - User-defined errors are particularly useful in situations where you want to handle application-specific error conditions gracefully. 
# - They make your code more expressive and provide a structured way to manage exceptional situations.
# - You can create multiple custom exception classes for different error scenarios in your application and raise them when necessary.
# 
# 
# 
# 
# 
# 

# In[70]:


# general syntax to create an exception
class ExceptionName(Exception):
    pass
  


# In[15]:


class MyException(Exception):
    def __init__(self,message):
        super().__init__(message)


# In[16]:


try:
    if 0 == 0:
        raise MyException("kuch")
except :
    print("handled")


# In[35]:


def divide(a, b):
    if a == 0 or b == 0:
        raise MyException("Hello Dear ,dont input Zero.")
    return a/b


# In[36]:


divide(0,88)


# In[37]:


try : 
    print(divide(0,8))
except MyException as e :
    print(e.args)


# In[38]:


try : 
    print(divide(0,5.0))
except MyException as e :
    print(e.args)


# In[29]:


class CustomError(Exception):
    pass


# In[39]:


age = int(input("Enter your age: "))
    
if age < 18:
    raise CustomError("You are not eligible.")
else:
    print("YOU are eligible")


# In[76]:



try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        raise CustomError("You are not eligible.")
    else:
        print("YOU are eligible")
except CustomError as e:
    print(f"Custom Error: {e}")


# In[ ]:





# ## Mini Project :

# In[48]:


class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal")
        self.balance -= amount

    def get_balance(self):
        return self.balance


# In[74]:


# Main program
if __name__ == "__main__":
    accounts = {}

    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                print("Account already exists.")
            else:
                initial_balance = float(input("Enter initial balance: "))
                accounts[account_number] = BankAccount(account_number, initial_balance)
                print("Account created successfully.")
        
        elif choice == "2":
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                amount = float(input("Enter the deposit amount: "))
                try:
                    accounts[account_number].deposit(amount)
                    print("Deposit successful.")
                except ValueError as e:
                    print(f"Deposit failed: {e}")
            else:
                print("Account not found.")
        
        elif choice == "3":
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                amount = float(input("Enter the withdrawal amount: "))
                try:
                    accounts[account_number].withdraw(amount)
                    print("Withdrawal successful.")
                except (ValueError, InsufficientFundsError) as e:
                    print(f"Withdrawal failed: {e}")
            else:
                print("Account not found.")
        
        elif choice == "4":
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                balance = accounts[account_number].get_balance()
                print(f"Account balance: {balance:.2f}")
            else:
                print("Account not found.")
        
        elif choice == "5":
            print("Exiting the banking system.")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")


# In[ ]:




