#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###heritage###
def heritage(i,j):
    k=i%j
    return k

res=heritage(1256983,28)
print('remaining coins:'+str(res))


# In[ ]:


12**52%15<8 or 3**5>100


# In[ ]:


5*3**3 != 900/75


# In[ ]:


###'[[]]' 'PYTHON'##

print('[[]]'[0:2:1]+'PYTHON'+'[[]]'[-1]*2)

###'Python'###

print('Python'[4:6:1]*4)

###'Perl'###
print('Perl'[2:3]*6)


# In[ ]:


###methods###

print('python'[0:3].upper()+'python'[3:6])

print('python'[0:1]*len('python'))

print('git'[0:1]*len('git'))


# In[ ]:


###What causes error###
"""
print(7+3*2)returns an integer 13
print('7'+str(3*2))returns a string '76'
print('7'+'3*2')returns an string '73*2'
print('7'+3*2) causes error because it is
only possible to concatenate the same data types
"""


# In[ ]:


###format###

hobby='skiing'
print('My hobby is {0}.'.format(hobby))

date='2018-11-01'
print('{0}/{1}'.format(date[8:10],date[5:7]))


# In[ ]:


###lists###

hobbies=[]
hobbies.append('skiing')
hobbies.append('singing')
hobbies.append('painting')
hobbies.append('reading')
print(hobbies)
print(hobbies[0])
print(hobbies[3])
del hobbies[3]
print(hobbies)


# In[ ]:


###cities###

cities=['Prague', 'Brno', 'Ostrava',
        'Plzen', 'Liberec', 'Olomouc', 
        'Usti nad Labem', 'Hradec Kralove',
        'Ceske Budejovice', 'Pardubice']
cities.sort()
print(cities)

string_cities="*".join(cities)
print(string_cities)


# In[6]:


###Zen of Python###

zen = "Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"
set(zen)

alphabet=set('abcdefghijklmnopqrstuvwxyz')

not_present=alphabet.difference(zen)

print(not_present)



# In[76]:


###dictionary###

d={'payton':'An interpreted,object-oriented programming language'}

d={value:key for key, value in d.items()}

d.update({'An interpreted,object-oriented programming language':'Python'})

d={value:key for key, value in d.items()}



###name: telephone###
name = ['Lenka','Lucie','Jana']
surname = ['Novakova', 'Vomackova', 'Sucha']
number = [777555333, 666999222, 333444999]

seznam = {name[0]+surname[0]:number[0],name[1]+surname[1]:number[1],name[2]+surname[2]:number[2]}


# In[67]:


###dictionary John Doe###
info = {('Name', 'Surname'): ('John','Doe')}
x = list(info.values())
John = x[0][0]
Doe = x[0][1]
John + '_' + Doe

