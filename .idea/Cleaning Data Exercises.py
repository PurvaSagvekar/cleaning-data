#!/usr/bin/env python
# coding: utf-8

# # Cleaning Data Exercises
# 
# For the exercises, you will be cleaning data in your chosen data set. [Towards Data Science](https://towardsdatascience.com/data-cleaning-in-python-the-ultimate-guide-2020-c63b88bf0a0d) outlines the steps we should take to clean data using a different data set from Kaggle. While you should use this article as a reference, make sure not to copy paste as the two data sets are very different!
# 
# To start cleaning data, we first need to create a dataframe from the CSV and print out any relevant info to make sure our dataframe is ready to go.

# In[1]:


# Import pandas and any other libraries you need here. HINT: Check out the article to see what they imported to get started!

# Create a new dataframe from your CSV
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.mlab as mlab
import matplotlib


# In[2]:


df = pd.read_csv("Reviews.csv")


# In[3]:


# Print out any information you need to understand your dataframe
df.info()


# In[4]:


df.head()


# In[5]:


df.tail()


# Now you have a dataframe set up, you are ready to dive in and start cleaning!

# ## Missing Data
# 
# In the Towards Data Science article, they list 3 techniques for detecting any missing data frame. Try all three before deciding on a way to solve any missing data issues.

# In[6]:


# Plot a heatmap of any missing data
plt.figure(figsize=(10,8))


# In[7]:


cols = df.columns[:11]


# In[8]:


colours = ['#000099', '#ffff00'] # specify colours: yellow - missing. blue - not missing


# In[9]:


plt.figure(figsize=(10,8))
sns.heatmap(df[cols].isna(), cmap=sns.color_palette(colours))


# In[10]:


# Try out a missing data percentage list! 
plt.figure(figsize=(10,8))
missing_by_rowmissing  = df.isna().sum(axis='columns')
missing_by_rowmissing .hist(bins=50)


# In[11]:


for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# In[12]:


# Plot a missing data histogram
plt.figure(figsize=(10,8))
for col in df.columns:
    missing = df[col].isnull()
    num_missing = np.sum(missing)
    
    if num_missing > 0:  
        print('created missing indicator for: {}'.format(col))
        df['{}_ismissing'.format(col)] = missing


# then based on the indicator, plot the histogram of missing values
ismissing_cols = [col for col in df.columns if 'ismissing' in col]
df['num_missing'] = df[ismissing_cols].sum(axis=1)

df['num_missing'].value_counts().reset_index().sort_values(by='index').plot.bar(x='index', y='num_missing')


# Now that you have tried all 3 techniques for detecting missing data, did you find any? Reading through the article, which solution do you think will help you clean the data set and handle the missing data? Try out your solution below!

# In[13]:


# Handle any missing data in your dataframe.


# ## Irregular Data
# 
# With missing data out of the way, turn your attention to any outliers. Just as we did for missing data, we first need to detect the outliers. The article outlines the top techniques for finding outliers in a dataset.

# In[14]:


# Plot a histogram to see if there are any outliers.
plt.figure(figsize=(10,8))
df['Rating'].hist(bins=100)


# In[15]:


plt.figure(figsize=(10,8))
df.boxplot(column=['Rating'])


# In[16]:


# Use the describe() method
df['Rating'].describe()


# In[17]:


# Plot a bar chart
plt.figure(figsize=(10,8))
df['Rating'].value_counts().plot.bar()


# Which of the three techniques helped you find any outliers? Now that you have found outliers, what will you do to solve the problem?

# In[18]:


# Handle any outliers in your dataframe


# ## Unnecessary Data
# 
# Unnecessary data could be duplicates, irrelevant, or any uninformative data. Dive into each type of unnecessary data to see if there is any in the data set. Make sure to make note of how you would handle each type of unnecessary data.

# In[19]:


# Look for any irrelevant data in the dataframe. How will you handle it?


# In[20]:


# Look for duplicates. How will you handle any duplicates?
df_dedupped = df.drop('Clothing ID', axis=1).drop_duplicates()

# there were duplicate rows
print(df.shape)
print(df_dedupped.shape)


# In[21]:


# Think about what data in the dataframe may be uninformative. Make note here of what situations may render data uninformative and how you would handle it?


# ## Inconsistent Data
# 
# Inconsistent data is anything that messes with your model. This is likely due to inconsistent formatting and can be addressed by re-formatting all values in a column or row.

# In[22]:


df['Department Name'].value_counts(dropna=False)


# In[23]:


# Try to convert all the strings in a column to lower or upper case. 
df['Department Name_upper'] = df['Department Name'].str.upper()
df['Department Name_upper'].value_counts(dropna=False)


# In[ ]:




