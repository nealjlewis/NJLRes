
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'homeworkTitle.py', '')


# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[2]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file= "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv (file)


# ## Player Count

# * Display the total number of players
# 

# In[3]:


#Total number of Unique Players
TP = purchase_data["SN"].value_counts()
#Find Count of Unique Items
UP = TP.count()
UP


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[4]:


Summ = purchase_data.describe()
Summ


# In[5]:


purchase_data.head()


# In[6]:


#Average Age
average_age = purchase_data["Age"].mean()
average_age


# In[7]:


#Get all Unique Items
Items = purchase_data["Item Name"].value_counts()
#Find Count of Unique Items
UItems = Items.count()
UItems


# In[8]:


# Average Price
average_price = purchase_data["Price"].mean()
average_price


# In[9]:


summary_df = pd.DataFrame({"average_price": [average_price],
                           "Unique Items": [UItems],
                           "Avg Age": [average_age]})
                           
print(summary_df)


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[10]:


# Gender Count of Players
gendercount = purchase_data["Gender"].value_counts()
gendercount

Gender_count = pd.DataFrame(gendercount)
Gender_count.head()


# In[11]:


#Gender %  Total Users
GenderPer1 = Gender_count/780
GenderPer2 = GenderPer1 *100
pd.options.display.float_format = '{:.2f}%'.format
GenderPer2


# In[12]:


#Gender %  Gender Unique 
GenderPer3 = Gender_count/UP
GenderPer4 = GenderPer3 *100
pd.options.display.float_format = '{:.2f}%'.format
GenderPer4


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[13]:


#Male Data
MaleData = purchase_data.loc[purchase_data["Gender"] == "Male", :]

MaleData.describe()


# In[14]:


#Get Male Price per User
MAvgPrice = MaleData["Price"].mean()
MAvgPrice


# In[15]:


# Male Purchase Count
MTotal = MaleData["Price"].sum()
MTotal


# In[16]:


# Male User Count 
MUser = MaleData["SN"].count()
print(MUser)


# In[17]:


# Highest Price Male
MHC = MaleData["Price"].max()
MHC


# In[18]:


#Lowest Price Male 
MLC = MaleData["Price"].min()
MLC


# In[19]:


#Purchae Total per male
MPP = MTotal/MUser
pd.options.display.float_format = '{:.2f}'.format
MPP


# In[20]:


#Male Dataframe
Msummary_df = pd.DataFrame({"Purchase Per Male": [MPP],
                           "Price Per Male": [MAvgPrice],
                           "Male User": [MUser],
                           "Male Total":[MTotal],})
print(Msummary_df)


# In[21]:


# Male Summary
MaleSumm = MaleData.describe()
pd.options.display.float_format = '{:.2f}'.format


# In[22]:


#Purchase Total Per Male 
#infom_pd = pd.DataFrame(MaleData, columns=["SN","Price"]).sum
#print (infom_pd)


# In[23]:


#Get Female Dataframe
FeMaleData = purchase_data.loc[purchase_data["Gender"] == "Female", :]

FeMaleData.describe()


# In[24]:


#Get Female Price per User
FAvgPrice = FeMaleData["Price"].mean()
FAvgPrice


# In[25]:


# Female Purchase Count
FTotal = FeMaleData["Price"].sum()
FTotal


# In[26]:


# Female User Count 
FUser = FeMaleData["SN"].count()
print(FUser)


# In[27]:


#Female Datafram
Fsummary_df = pd.DataFrame({"Femal Player Total": [FUser],
                           "Price Per FeMale": [FAvgPrice],
                           "Purchase Per Femail": [FAvgPrice],
                           "Female Total":[FTotal],})
print(Fsummary_df)


# In[28]:


# Highest Price Female
FHC = FeMaleData["Price"].max()
FHC


# In[29]:


# Lowest Price Female
FLC = FeMaleData["Price"].min()
FLC


# In[30]:


#Purchae Total per Female
#infof_pd = pd.DataFrame(FeMaleData, columns=["SN","Price"]).sum
#infof_pd


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[31]:


# Establish bins for ages
bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


# In[32]:


raw_data = {
    'bins': [9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999], 
    'group_names': ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]}
    


# In[33]:


#Show Bin info
df = pd.DataFrame(raw_data)
df


# In[34]:


#Use pd cut 
pd.cut(df["bins"], bins, labels=group_names)


# In[35]:


#Categorize the existing players using the age bins
purchase_data["Age Group"] = pd.cut(purchase_data["Age"], bins, labels=group_names)
purchase_data.head()


# In[36]:


# Create a GroupBy object based upon "Age Group"
Agegroup = purchase_data.groupby("Age Group")


# In[37]:


# Find how many players are in each age group
print(Agegroup["Age Group"].count())


# In[38]:


#Average Price by Age Group
Agegroup[["SN","Price", "Age Group"]].mean()


# In[39]:


# Percent of Age Group
Per1=(Agegroup["Age Group"].count())
pd.options.display.float_format = '{:.2f}%'.format
Per1/780 *100


# In[40]:


#Age Group Demographics
pd.options.display.float_format = '{:.2f}'.format
Agegroup.describe()


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[41]:


#Average Price by Age Group
Agegroup[["SN","Price", "Age Group"]].mean()


# In[42]:


#Average Price per Person -age
print(Agegroup['Price'].mean())


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[43]:


# Create summary data fram and sort in descending order. Display Preview
TopSpend = purchase_data.sort_values("Price", ascending=False)

TopSpend.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[44]:


# Retrieve ITem ID, Name, and Price
PopT = purchase_data[["Item ID", "Item Name", "Price"]]
PopT.head()


# In[45]:


#Item Count
ItemCount = PopT["Item Name"].value_counts()
ItemCount.head()


# In[46]:


# Group by Item Name
Itemgroup = PopT.groupby(["Item ID", "Item Name"])
#Itemgroup.head(5)


# In[47]:


#Item Count
Itemcount =(Itemgroup["Item ID","Item Name"].count())
Itemcount.head()


# In[48]:


ItemD = Itemgroup.mean()
pd.options.display.float_format = '{:.2f}'.format
ItemD.head()


# In[49]:


# Item Sum 
Itemf = Itemgroup.sum()
Itemf.head()


# In[50]:


#total purchase value
TTV["Total"] = Itemgroup["Item ID"] * Itemgroup["Price"]


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[ ]:


TopProf = Itemgroup.sort_values("Price", ascending=False)

