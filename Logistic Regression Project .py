#!/usr/bin/env python
# coding: utf-8

# # Logistic Regression
# 
# In this project we will be working with a fake advertising data set, indicating whether or not a particular internet user clicked on an Advertisement. We will try to create a model that will predict whether or not they will click on an ad based off the features of that user.
# 
# This data set contains the following features:
# 
# * 'Daily Time Spent on Site': consumer time on site in minutes
# * 'Age': cutomer age in years
# * 'Area Income': Avg. Income of geographical area of consumer
# * 'Daily Internet Usage': Avg. minutes a day consumer is on the internet
# * 'Ad Topic Line': Headline of the advertisement
# * 'City': City of consumer
# * 'Male': Whether or not consumer was male
# * 'Country': Country of consumer
# * 'Timestamp': Time at which consumer clicked on Ad or closed window
# * 'Clicked on Ad': 0 or 1 indicated clicking on Ad
# 
# ## Import Libraries
# 
# **Import a few libraries you think you'll need (Or just import them as you go along!)**

# In[61]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Get the Data
# **Read in the advertising.csv file and set it to a data frame called ad_data.**

# In[62]:


train = pd.read_csv("C:\\Users\\engrz\\Downloads\\Compressed\\Assignment 1\\advertising.csv")


# **Check the head of ad_data**

# In[63]:


train.head()


# ** Use info and describe() on ad_data**

# In[64]:


train.info()


# In[65]:


train.describe()


# ## Exploratory Data Analysis
# 
# Let's use seaborn to explore the data!
# 
# Try recreating the plots shown below!
# 
# ** Create a histogram of the Age**

# In[66]:


sns.set_style("whitegrid")
sns.distplot(train['Age'],kde=False,bins=30,hist_kws={"alpha":0.75})


# **Create a jointplot showing Area Income versus Age.**

# In[67]:


sns.jointplot(x="Age",y="Area Income",data=train)


# **Create a jointplot showing the kde distributions of Daily Time spent on site vs. Age.**

# In[68]:


sns.jointplot(x="Age",y="Daily Time Spent on Site",data=train,kind="kde",color="green")


# ** Create a jointplot of 'Daily Time Spent on Site' vs. 'Daily Internet Usage'**

# In[69]:


sns.jointplot(x="Daily Time Spent on Site",y="Daily Internet Usage",data=train,color="green")


# ** Finally, create a pairplot with the hue defined by the 'Clicked on Ad' column feature.**

# In[70]:


sns.pairplot(train ,hue="Clicked on Ad")


# # Logistic Regression
# 
# Now it's time to do a train test split, and train our model!
# 
# You'll have the freedom here to choose columns that you want to train on!

# ** Split the data into training set and testing set using train_test_split**

# In[71]:


from sklearn.model_selection import train_test_split


# In[72]:


X = train[["Daily Time Spent on Site", 'Age', 'Area Income','Daily Internet Usage', 'Male']]


# In[73]:


Y = train["Clicked on Ad"]


# In[74]:


X_train, X_test, Y_train, Y_test = train_test_split(X,train["Clicked on Ad"],test_size=0.30,random_state=50)


# ** Train and fit a logistic regression model on the training set.**

# In[75]:


from sklearn.linear_model import LogisticRegression


# In[76]:


model = LogisticRegression()
model.fit(X_train,Y_train)


# ## Predictions and Evaluations
# ** Now predict values for the testing data.**

# In[77]:


prediction = model.predict(X_test)


# ** Create a classification report for the model.**

# In[78]:


from sklearn.metrics import classification_report


# In[79]:


print(classification_report(Y_test,prediction))


# ## Great Job!

# In[ ]:




