#!/usr/bin/env python
# coding: utf-8

# In[3]:


###Error corretion 1###

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ' + seasons[3])


# In[7]:


###Error correction 2###

for number in range(10):
    message = "message: "
    # use a if the number is a multiple of 3, otherwise use b
    if (number % 3) == 0:
        message = message + "a"
    else:
        message = message + "b"
    print(message)


# In[30]:


###Exceptions###

x = list(input('Your name: '))
for i in x:
    try:
        int(i)
        raise Exception('Your name cannot include a number.')
    except ValueError:
        pass
if ' ' in x:
    raise Exception('Your name includes spaces, remove them.')
if x[0].islower():
    raise Exception("Your name cannot with lower letter.")
else:
    pass


# In[66]:


###division###


def division():
    flag = False
    while flag is False:
        x = input('Write dividend: ')
        y = input('Write divisor: ')
        try:
            dividend = int(x)
            divisor = int(y)
            res = dividend // divisor
            flag = True
        except ValueError:
            print('Dividend or divisor is not a number.')
        except ZeroDivisionError:
            print('You cannot divide by zero.')
    return res
division()


# In[74]:


###Debuging###

year = int(input("Greetings! What is your year of origin? "))
if year <= 1900:
    print ("Woah, that's the past!")
elif (year > 1900) and (year < 2020):
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")

