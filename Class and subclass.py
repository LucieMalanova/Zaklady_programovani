#!/usr/bin/env python
# coding: utf-8

# In[8]:


###class###
class Animal:
    def __init__(self, name):
        self.__myname = name
    def get_name(self):
        print(self._Animal__myname)


# In[17]:


###subclass###
class Cat(Animal):
    def __init__(self, name, purr_sound):
        Animal.__init__(self, name)
        self.__purr_sound = purr_sound
    def purr(self):
        print(self._Cat__purr_sound)
        
cat_caller = Cat('Sojinek', 'catkittycatcatkittycatcat')
cat_caller.get_name()
cat_caller.purr()

