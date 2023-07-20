#!/usr/bin/env python
# coding: utf-8

# ## 1. What exactly is []?
# ## Ans :
# [] it called as list

# ## 2. In a list of values stored in a variable called spam, how would you assign the value &#39;hello&#39; as the
#  ## third value? (Assume [2, 4, 6, 8, 10] are in spam.)
#  ### Ans:

# In[1]:


spam = [2, 4, 6, 8, 10]
spam[2] = 'hello'
spam


# In[2]:


spam = [2, 4, 6, 8, 10]
spam.insert(2,'hello')
spam


# ## Let&#39;s pretend the spam includes the list [&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;] for the next three queries.
# ## 3. What is the value of spam[int(int(&#39;3&#39; * 2) / 11)]?
# ### Ans:

# In[3]:


spam = ['a', 'b','c','d']
spam[int(int('3' * 2) / 11)]


# ## 4. What is the value of spam[-1]?
# ### Ans:

# In[4]:


spam[-1]


# ## 5. What is the value of spam[:2]?
# ### Ans:
# 

# In[5]:


spam[:2]


# ## Let's pretend bacon has the list [3.14, 'cat' 11, 'cat' True] for the next three questions.
# ## 6. What is the value of bacon.index('cat')?
#  ### Ans:

# In[6]:


bacon =[3.14, 'cat' ,  11, 'cat', True]
bacon.index('cat')


# ## 7. How does bacon.append(99) change the look of the list value in bacon?
# ### Ans

# In[ ]:





# ## 8. How does bacon.remove('cat') change the look of the list in bacon?
# ### Ans:
# 

# In[7]:


bacon.remove('cat')
bacon


# ## 9. What are the list concatenation and list replication operators?
# * -> is list replication operatotor
# + -> is list cancatination operator
# ### Ans:
# 

# In[8]:


l1 = [2,4]
l2 = [1,5]
l1+l2


# In[9]:


l1 = [1,3]
l1*2


# ## 10. What is difference between the list methods append() and insert()?
# append() ->Appends object to the end of the list
# 
# insert() -> Insert object before index
# ### Ans:

# In[10]:


bacon =[3.14, 'cat' ,  11, 'cat', True]
bacon.append(99)
bacon


# In[11]:


bacon.insert(3,'hello')
bacon


# In[ ]:





# ## 11. What are the two methods for removing items from a list?
# remove(item) - removeds first occurence of a item
# 
# pop() - Remove and returns item at index (default last).
# 
# del(list) - deletes the list
# ### Ans:

# In[15]:


bacon =[3.14, 'cat' ,  11, 'cat', True]
bacon.remove('cat')
bacon


# In[17]:


bacon =[3.14, 'cat' ,  11, 'cat', True]
bacon.pop()
bacon


# ## 12. Describe how list values and string values are identical.
# ### Ans
# 1. Both lists and strings can be passed to len()
# 2. Have indexes and slices
# 3. Can be used in for loops
# 4. Can be concatenated or replicated
# 5. Can be used with the in and not in operators
# 
# ## 13. What's the difference between tuples and lists?
# ## Ans:
# Lists :
# are mutable - they can have values added, removed, or changed. 
# lists use the square brackets, [ and ]
# Tuples :
# are immutable; they cannot be changed at all. 
# Tuples are written using parentheses, ( and ) while
# 
# ## 14. How do you type a tuple value that only contains the integer 42?
# ### Ans:

# In[18]:


t = (42)
t


# ## 15. How do you get a list value's tuple form? How do you get a tuple value's list form?
# By using tuple() and list() functions
# ### Ans:

# In[19]:


l1 = [1,2,3]
l = tuple(l1)
l


# In[21]:


t1 = (1,2,3)
l =list[t1]
l


# ## 16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
# ### Ans:
# They contain references to list values
# 
# ## 17. How do you distinguish between copy.copy() and copy.deepcopy()?
# ### Ans:
# The copy.copy() function will do a shallow copy of a list, 
# The copy.deepcopy() function will do a deep copy of a list. only copy.deepcopy() will duplicate any lists inside the 
# list

# In[ ]:




