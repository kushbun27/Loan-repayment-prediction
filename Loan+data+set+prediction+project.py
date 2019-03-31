
# coding: utf-8

# ___
# 
# ___
# # Random Forest Project - Solutions
# 
# For this project we will be exploring publicly available data from [LendingClub.com](www.lendingclub.com). Lending Club connects people who need money (borrowers) with people who have money (investors). Hopefully, as an investor you would want to invest in people who showed a profile of having a high probability of paying you back. We will create a model that will help predict this.
# 
# Here are what the columns represent:
# * credit.policy: 1 if the customer meets the credit underwriting criteria of LendingClub.com, and 0 otherwise.
# * purpose: The purpose of the loan (takes values "credit_card", "debt_consolidation", "educational", "major_purchase", "small_business", and "all_other").
# * int.rate: The interest rate of the loan, as a proportion (a rate of 11% would be stored as 0.11). Borrowers judged by LendingClub.com to be more risky are assigned higher interest rates.
# * installment: The monthly installments owed by the borrower if the loan is funded.
# * log.annual.inc: The natural log of the self-reported annual income of the borrower.
# * dti: The debt-to-income ratio of the borrower (amount of debt divided by annual income).
# * fico: The FICO credit score of the borrower.
# * days.with.cr.line: The number of days the borrower has had a credit line.
# * revol.bal: The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle).
# * revol.util: The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available).
# * inq.last.6mths: The borrower's number of inquiries by creditors in the last 6 months.
# * delinq.2yrs: The number of times the borrower had been 30+ days past due on a payment in the past 2 years.
# * pub.rec: The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments).

# # Import Libraries
# 

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# ## Get the Data
# 
# 

# In[2]:

loans = pd.read_csv('loan_data.csv')


# ** Check out the info(), head(), and describe() methods on loans.**

# In[3]:

loans.info()


# In[4]:

loans.describe()


# In[5]:

loans.head()


# # Exploratory Data Analysis
# 
# Let's do some data visualization! We'll use seaborn and pandas built-in plotting capabilities, but feel free to use whatever library you want. Don't worry about the colors matching, just worry about getting the main idea of the plot.
# 
# ** Create a histogram of two FICO distributions on top of each other, one for each credit.policy outcome.**
# 

# In[6]:

plt.figure(figsize=(10,6))
loans[loans['credit.policy']==1]['fico'].hist(alpha=0.5,color='blue',
                                              bins=30,label='Credit.Policy=1')
loans[loans['credit.policy']==0]['fico'].hist(alpha=0.5,color='red',
                                              bins=30,label='Credit.Policy=0')
plt.legend()
plt.xlabel('FICO')


# ** Create a similar figure, except this time select by the not.fully.paid column.**

# In[7]:

plt.figure(figsize=(10,6))
loans[loans['not.fully.paid']==1]['fico'].hist(alpha=0.5,color='blue',
                                              bins=30,label='not.fully.paid=1')
loans[loans['not.fully.paid']==0]['fico'].hist(alpha=0.5,color='red',
                                              bins=30,label='not.fully.paid=0')
plt.legend()
plt.xlabel('FICO')


# ** Create a countplot using seaborn showing the counts of loans by purpose, with the color hue defined by not.fully.paid. **

# In[8]:

plt.figure(figsize=(11,7))
sns.countplot(x='purpose',hue='not.fully.paid',data=loans,palette='Set1')


# 

# In[9]:

sns.jointplot(x='fico',y='int.rate',data=loans,color='purple')


# ** Create the lmplots to see if the trend differed between not.fully.paid and credit.policy. **

# In[10]:

plt.figure(figsize=(11,7))
sns.lmplot(y='int.rate',x='fico',data=loans,hue='credit.policy',
           col='not.fully.paid',palette='Set1')


# # Setting up the Data
# 
# 
# **Check loans.info() again.**

# In[11]:

loans.info()


# ## Categorical Features
# 
# Notice that the **purpose** column as categorical
# 
# That means we need to transform them using dummy variables so sklearn will be able to understand them. Let's do this in one clean step using pd.get_dummies.
# 
# 
# 

# In[12]:

cat_feats = ['purpose']


# 

# In[13]:

final_data = pd.get_dummies(loans,columns=cat_feats,drop_first=True)


# In[14]:

final_data.info()


# ## Train Test Split
# 
# Now its time to split our data into a training set and a testing set!
# 
# ** Use sklearn to split your data into a training set and a testing set as we've done in the past.**

# In[15]:

from sklearn.model_selection import train_test_split


# In[16]:

X = final_data.drop('not.fully.paid',axis=1)
y = final_data['not.fully.paid']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)


# ## Training a Decision Tree Model
# 
# 
# ** Import DecisionTreeClassifier**

# In[17]:

from sklearn.tree import DecisionTreeClassifier


# **Create an instance of DecisionTreeClassifier() called dtree and fit it to the training data.**

# In[18]:

dtree = DecisionTreeClassifier()


# In[19]:

dtree.fit(X_train,y_train)


# ## Predictions and Evaluation of Decision Tree
# **Create predictions from the test set and create a classification report and a confusion matrix.**

# In[20]:

predictions = dtree.predict(X_test)


# In[21]:

from sklearn.metrics import classification_report,confusion_matrix


# In[22]:

print(classification_report(y_test,predictions))


# In[23]:

print(confusion_matrix(y_test,predictions))


# ## Training the Random Forest model
# 
# Now its time to train our model!
# 
# **Create an instance of the RandomForestClassifier class and fit it to our training data from the previous step.**

# In[24]:

from sklearn.ensemble import RandomForestClassifier


# In[25]:

rfc = RandomForestClassifier(n_estimators=600)


# In[26]:

rfc.fit(X_train,y_train)


# ## Predictions and Evaluation
# 
# Let's predict off the y_test values and evaluate our model.
# 
# ** Predict the class of not.fully.paid for the X_test data.**

# In[27]:

predictions = rfc.predict(X_test)


# **Now create a classification report from the results. Do you get anything strange or some sort of warning?**

# In[28]:

from sklearn.metrics import classification_report,confusion_matrix


# In[29]:

print(classification_report(y_test,predictions))


# **Show the Confusion Matrix for the predictions.**

# In[30]:

print(confusion_matrix(y_test,predictions))


# 

# In[36]:




# 
