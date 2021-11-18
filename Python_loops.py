#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###names###

names_list = ['Jiri', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef', 
'Pavel', 'Martin', 'Jaroslav', 'Tomas', 'Eva', 'Miroslav', 
'Hana', 'Anna', 'Zdenek', 'Frantisek', 'Vaclav', 'Michal', 
'Lenka', 'Katerina']

x = str(input('Your name: '))

if x in names_list:
    print('Your name is in top 20!')
else:
    print('Sorry, at least your name is original.')


# In[ ]:


###smycky###

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 
'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 
'j':'juliett', 'k':'kilo', 'l':'lima', 'm':'mike', 
'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 
'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 
'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 
'z':'zulu'}

x = str(input('Your name: '.lower()))
for letter in x:
    print(d[letter])
    


# In[ ]:


###transposition###

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
b = [[],
     [],
     []]

for i in range(3):
    for j in range(3):
        b[i].append(a[j][i])
        
for row in b:
    print(row)


# In[ ]:


shopping_list = ['yoghurt','cereals','apples','bread']

item = str(input('new item: '))
for i in range(len(shopping_list)):
    if item == shopping_list[i]:
        print(item)
        break
    if i == (len(shopping_list)-1):
        shopping_list.append(item)
        print(shopping_list)
        

        


# In[ ]:


###second power is my favourite number!###

list_a = list(range(5))
list_b = [str(x**2)+ ' is my favourite number!' for x in list_a]

print(list_a)
print(list_b)


# In[ ]:


###A position###

input_list = list(str(input('write sequence of letters: ').upper()))
position_list = [position for position, A in enumerate(input_list) if A=='A']
position_list


# In[5]:


###scores###

scores = {'John' : 10, 'Emily' : 35, 'Matthew' : 50}
scores_triple = {list(scores.keys())[i]: list(scores.values())[i]*3 for i in range(len(scores))}
print(scores_triple)

