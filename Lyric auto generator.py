#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tkinter as tk
import random

# List of random lyrics
lyrics = [
    "Ek ho gaye hum aur tum",
    "Humma humma humma…",
    "Toh udd gayi ninde re",
    "Hey humma…",
    "Ek hogaye hum aur tum",
    "Toh udd gayi ninde re",
    "Aur khanki payal masti mein",
    "Toh kangan…"
]

last_lyric = None

def generate_lyric():
    global last_lyric
    random_lyric = random.choice(lyrics)
    
    # Ensure the new lyric is different from the last one
    while random_lyric == last_lyric:
        random_lyric = random.choice(lyrics)
    
    last_lyric = random_lyric
    result_label.config(text=random_lyric)

# Create main window
root = tk.Tk()
root.title("Random Lyric Generator")

# Set background color to light blue
root.configure(bg="#ADD8E6")

# Create label to display random lyric
result_label = tk.Label(root, font=("Helvetica", 14), wraplength=300, justify="center", bg="#ADD8E6")
result_label.pack(pady=20)

# Create button to generate random lyric
generate_button = tk.Button(root, text="Generate Lyric", command=generate_lyric, bg="#000000", fg="#FFFFFF", font=("Helvetica", 12), width=15, height=2)
generate_button.pack(pady=10)

# Run the GUI
root.mainloop()


# In[ ]:


import tkinter as tk
from tkinter import simpledialog
import random

# List of random lyrics
lyrics = [
    "Ek ho gaye hum aur tum",
    "Humma humma humma…",
    "Toh udd gayi ninde re",
    "Hey humma…",
    "Ek hogaye hum aur tum",
    "Toh udd gayi ninde re",
    "Aur khanki payal masti mein",
    "Toh kangan…"
]

last_lyric = None

def generate_lyric():
    global last_lyric
    random_lyric = random.choice(lyrics)
    
    # Ensure the new lyric is different from the last one
    while random_lyric == last_lyric:
        random_lyric = random.choice(lyrics)
    
    last_lyric = random_lyric
    result_label.config(text=random_lyric)

def add_new_lyric():
    new_lyric = simpledialog.askstring("Add New Lyric", "Enter the new lyric:")
    
    if new_lyric and new_lyric not in lyrics:
        lyrics.append(new_lyric)
        result_label.config(text="New lyric added successfully!")
    elif new_lyric:
        result_label.config(text="Lyric already exists!")

# Create main window
root = tk.Tk()
root.title(" Boom")

# Set background color to light blue
root.configure(bg="#ADD8E6")

# Create label to display random lyric
result_label = tk.Label(root, font=("Helvetica", 14), wraplength=300, justify="center", bg="#ADD8E6")
result_label.pack(pady=20)

# Create button to generate random lyric
generate_button = tk.Button(root, text="Generate Lyric", command=generate_lyric, bg="#000000", fg="#FFFFFF", font=("Helvetica", 12), width=15, height=2)
generate_button.pack(pady=10)

# Create button to add new lyric
add_button = tk.Button(root, text="Add New Lyric", command=add_new_lyric, bg="#008000", fg="#FFFFFF", font=("Helvetica", 12))
add_button.pack(pady=5)

# Run the GUI
root.mainloop()


# In[ ]:




