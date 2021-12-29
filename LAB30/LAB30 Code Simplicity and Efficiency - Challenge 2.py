#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Challenge 2


# In[4]:


import numpy as np
import pandas as pd


# In[5]:


import random
import sys
import string


# In[7]:


# The code below generates a given number of random strings that consists of numbers and lower case English 
# letters. You can also define the range of the variable lengths of the strings being generated.

# The code is functional but has a lot of room for improvement. Use what you have learned
# about simple and efficient code, refactor the code.


# In[9]:


def random_string_generator(length=12):
    ALPHA_NUM = [chr(item) for item in list(range(97,123)) + list(range(48,58))];
    return "".join(random.sample(ALPHA_NUM, length));


# In[10]:


def batch_string_generator(n_strings, min_len=8, max_len=12):
    if min_len > max_len:
        return sys.exit('Incorrect min and max string lengths. Try again.');
    else:
        var_len = [min_len 
            if min_len == max_len 
            else random.choice(range(min_len, max_len)) 
                for n in range(n_strings)];
        return list(map(random_string_generator, var_len));


# In[11]:


min_len = input('Enter minimum string length: ');
max_len = input('Enter maximum string length: ');
n_strings = input('How many random strings to generate? ');
print(batch_string_generator(int(n_strings), int(min_len), int(max_len)));

