#!/usr/bin/env python
# coding: utf-8

# In[5]:


###Agalma elegans###

(\w)\w+\s(\w+)
\1. \2

###zen of python###
(a\.)|(o\.) = 2 matches
\w = 653 matches
[Tt]{2} = 8 matches
[Tt]{1,2} = 67 matches


# In[27]:


import re
###type name###

only_letters = re.compile(r'\W|\s|\d')
first_uppercase = re.compile(r'^[a-z]')

def type_name():
    match = False
    while match is False:
        name = str(input('Type your name: '))
        out1 = bool(re.search(only_letters, name))
        out2 = bool(re.search(first_uppercase, name))
        if out1:
            print('Your name cannot include special characters')
        if out2:
            print('Your name has to start with uppercase letter.')
        if (not out1 and not out2):
            match = True
            print('Your name is OK.')
type_name()


# In[24]:


###only digits###
def only_digits(number):
    res = re.sub(r'\D', '', number)
    print(res)
    
only_digits('22eep22pp')

