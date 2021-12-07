#!/usr/bin/env python
# coding: utf-8

# In[7]:


###divide two numbers import module###
from Python_functions import divide

divide(12,2)


# In[11]:


###vowels and consonants count###
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("word", help="counts letters in word", type=str)
parser.add_argument("-c", help= "counts consonants")
parser.add_argument("-v", help= "counts vowels")
args = parser.parse_args()
vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_ct = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
if args.v:
    for letter in args.word:
        if letter in vowels:
            idx = alphabet.index(letter)
            alphabet_ct[idx] += 1
if args.c:
    for letter in args.word:
        if letter in consonants:
            idx = alphabet.index(letter)
            alphabet_ct[idx] += 1
            
for i in range(26):
    if alphabet_ct[i] != 0:
        print(alphabet[i],alphabet_ct[i])


# In[ ]:



###occurences###
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("str1", type=str)
parser.add_argument("str2", type=str)
args = parser.parse_args()

print("string " + args.str1 + " occured " + str((args.str2).count(str(args.str1))) + " times in string " + args.str2) 


# In[ ]:


###extract letter###

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("word", type=str)
parser.add_argument("letter", type=str)
args = parser.parse_args()

if args.letter in args.word:
    word_list = list(args.word)
    word_list.remove(args.letter)
    print(str(word_list))
else:
    print(args.word)


# In[17]:


###empty island###

file_path = r'C:\Users\lucin\OneDrive\Plocha\zaklady_programovani\list_of_things.tsv'
list_of_things = ['casserole','book','knife','water bottle','fishing rod']

with open(file_path, 'w', encoding= 'utf-8') as file:
    for i in range(len(list_of_things)):
        file.write(str(print(i+1,list_of_things[i] + '\n')))
        


# In[ ]:




