
# coding: utf-8

# In[4]:


#dependencies
import os 
import csv
import pandas as pd 
import numpy as np
Budget = os.path.join("..", "budget_data.csv")


# In[5]:


with open(Budget, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


# In[6]:


# total # of months 
Rows = sum(1 for line in open(Budget))
len(open(Budget).readlines())
len(pd.read_csv(Budget)) 


# In[7]:


#total net amount of profit/loss
with open('budget_data.csv', 'r') as f:
  next(f) 
  total = 0
  for row in csv.reader(f):
    total += float(row[1])
  print('The The net amount of profit is {}'.format(total))


# In[8]:


#avg chang in profit/losss between months 
with open('budget_data.csv', 'r') as f:
  next(f) 
  Average = 0
  for row in csv.reader(f):
    Average += float(row[1])/ Rows
  print('The average profit is {}'.format(Average))


# In[9]:


#Greatest increase in profits 
my_data = np.genfromtxt("budget_data.csv", delimiter=",", skip_header=True)
Profit =("max value element : ", my_data.max(axis=0)[1])
print('The highest profit is {}'.format(Profit))


# In[10]:


#greatest loss
my_data = np.genfromtxt("budget_data.csv", delimiter=",", skip_header=True)
Loss =("min value element : ", my_data.min(axis=0)[1])
print('The greatest loss is {}'.format(Loss))

