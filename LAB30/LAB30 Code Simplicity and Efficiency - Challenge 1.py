#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Challenge 1


# In[ ]:


"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')


# In[19]:


# first step, we ask for inputing both numbers and choice of calculation
def ask_for_input ():
    first_number = input('Please choose your first number (zero to five): ');
    calculation = input('What do you want to do? plus or minus: ');
    second_number = input('Please choose your second number (zero to five): ');
    return (first_number, calculation, second_number);


# In[20]:


# Check whether the input numbers are valid within the given set of numbers
def check_number_input (number):
    VALID_NUMBERS = ['zero', 'one', 'two', 'three', 'four', 'five'];
    return number in VALID_NUMBERS;


# In[27]:


# Check whether the choice of calculation is either a + or -
def check_calculation_input (calculation):
    VALID_CALCULATION = ['minus', 'plus'];
    return calculation in VALID_CALCULATION;


# In[22]:


# We combine both given numbers and the choice of calculation in one operation
def check_inputs (first_number, calculation, second_number):
    is_first_number_valid = check_number_input(first_number);
    is_calculation_valid = check_calculation_input(calculation);
    is_second_number_valid = check_number_input(second_number);
    
    return is_first_number_valid and is_calculation_valid and is_second_number_valid;


# In[23]:


# We complete the equation plus or minus of the the 2 numbers
def equation (first_number, calculation, second_number):
    NUMBERS_DICT = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5'};
    CALCULATION_DICT = {'minus': '-', 'plus': '+'};
    return eval("{} {} {}".format(NUMBERS_DICT[first_number], CALCULATION_DICT[calculation], NUMBERS_DICT[second_number]));


# In[24]:


# we reconvert the integer into a string 
def find_str_result (num_result):
    NUMBERS_DICT = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', 
                    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'};
    return NUMBERS_DICT[str(num_result)] if num_result >= 0 else "negative {}".format(NUMBERS_DICT[str(num_result)[-1]])


# In[25]:


def dumb_calculation ():
    print('Welcome to this calculator!');
    print('It can add and subtract whole numbers from zero to five');

    first_number, calculation, second_number = ask_for_input();
    valid_inputs = check_inputs(first_number, calculation, second_number);

    if not (valid_inputs):
        print("I am not able to answer this question. Check your input.");
    else:
        num_result = equation(first_number, calculation, second_number);
        result = find_str_result(num_result);
        print("{} {} {} equals {}".format(first_number, calculation, second_number, result));

    print("Thanks for using this calculator, goodbye :)")


# In[30]:


dumb_calculation();


# In[ ]:




