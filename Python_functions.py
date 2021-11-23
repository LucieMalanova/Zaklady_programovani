#!/usr/bin/env python
# coding: utf-8

# In[1]:


###division###

def divide(divident, divisor):
    res = divident/divisor
    return res
    
divide(16,20)
    


# In[21]:


###suma####

def suma(list_numbers):
    res = 0
    for item in list_numbers:
        res = res + item
    return(res)
      
    
suma([1, 2, 8, 4])


# In[28]:


###lambda###

compare_list = (lambda x: print('small list') if len(x) < 5 else print('big list'))
compare_list([4,5,6,7])


# In[32]:


###one parameter###

def string_upper_lower(string):
    lower_letters = 0
    upper_letters = 0
    for letter in string:
        if letter.islower():
            lower_letters += 1
        if letter.isupper():
            upper_letters += 1
        else:
            pass    
    return string, lower_letters, upper_letters
        
string_upper_lower('ahoj AAA:<>?:AAjak se mas')


# In[36]:


###two parameters###

def meal_vouchers(lunch_cost, voucher_value):
    
    pay_cash = lunch_cost % voucher_value
    num_vouchers = (lunch_cost - pay_cash)/voucher_value
    return num_vouchers, pay_cash

meal_vouchers(500, 74)


# In[42]:


###recursion###

def factorial(n):
    if n > 0:
        f_n_1 = factorial(n-1)
        f_n = n * f_n_1
        print(f_n)
        return f_n
    elif n == 0:
        return 1
    
factorial(50)
    

