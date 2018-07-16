
# coding: utf-8

# In[ ]:


#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.


# In[60]:


#dependencies
import os 
import csv


# In[63]:


#List of canidates who received votes
List = []
with open('election_data.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        List.append(row[2])
        
from collections import OrderedDict
OrderedDict((x, True) for x in List).keys()


# In[ ]:


# Percentage of voes Each Candidate won 
#import pandas as pd 
#df=pd.read_csv("election_data.csv", sep=',')
#df.groupby(['Candidate',]).apply(lambda x: x / x.sum()).
poll = os.path.join("..", "election_data.csv")
Rows = sum(1 for line in open(poll))
len(open(poll).readlines())
len(pd.read_csv(poll)) 


# In[ ]:


#Percentage of votes each canidate won
# number of rows 
poll = os.path.join("..", "election_data.csv")
=sum(1 for line in open(poll))
len(open(poll).readlines())
len(pd.read_csv(poll)) 
print(Rows)

#find % of votes
import pandas as pd 
#df=pd.read_csv("election_data.csv", sep=',')
#df.groupby(['Candidate',]).apply(lambda x: x / x.sum()).


# In[59]:


# Total number of votes each candidate won 
from collections import Counter
cnt = Counter()
f = open("election_data.csv")
reader = csv.reader(f, delimiter=",")
header = next(f) 

for row in reader:   
    cnt[row[2]] += 1 
    
print(cnt)


# In[61]:


## Winner of election 
with open('election_data.csv', 'r') as f:
      column = (row[2] for row in csv.reader(f))
      print("Winner of Election: {0}".format(Counter(column).most_common()[0][0]))

