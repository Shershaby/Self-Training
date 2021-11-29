#!/usr/bin/env python
# coding: utf-8

# ### Class Training

# In[ ]:


class living():
    def __init__(self, yes_or_no):
        self.living = yes_or_no
        
class cat(living):
    def __init__(self, s, f, h):
        super().__init__('3bas')
        self.namee = s
        self.agee = f
        self.type = h
    def printing(self):
        print(self.living)
        
kitty = cat('fawzy', 3, 'siamy')

kitty.printing()


# In[1]:


size = ['small', 'medium', 'large']
print(size)

price = {'small':15, 'medium':20, 'large':25}

extra_pep = {'small':2, 'medium':3, 'large':3}

user = input('Please choose your pizza size: ')

if user in size and user in price:
    print("good choice....")
    print("it will cost " + str(price[user]) + '$')
    
answer1 = input('Do you need extra Pepproni: ')
if answer1 == 'yes':
    z = price[user] + extra_pep[user]
    print(z,'$')
else:
    print("We are happy to serve you")

answer2 = input('Do you need extra Cheese: ')
if answer2 == 'yes':
    x = price[user] + extra_pep[user] + 1
    print(x,'$')        


# In[ ]:


a = 2021
x = input("Enter Your Name: ")
y = int(input("Enter your Age: "))

def year(age):
    s = a - y
    r = s + 100
    return r

print('Hey ' + x + '\nyou will turn 100 on ' + str(year(y)))

