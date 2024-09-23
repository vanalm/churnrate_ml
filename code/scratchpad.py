#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:29:34 2024

@author: jacobvanalmelo
"""
import time
#IMPORTS
print('importing libraries...')
now = time.time()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from scipy import stats

elapsed = time.time()-now
print(f"imports took {elapsed} seconds")

print("settings preferences...")
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)


now = time.time()
print(f"loading data...")
df= pd.read_csv("./data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

elapsed = time.time()-now
print(f"load data took {elapsed} seconds")


print('taking a look at the data...')
print(df.head())
print(df.info())
print(df.shape)
print(f"null data:\n{df.isnull().sum()}")


'''
So this is a warm up after a long haitus in ml/datascience (a year???) so lets be thorough and write it out.

Now I'm reading what all of the columns are to get my mind on the data.
CHURN is the target variable. it indicates whether a customer left within the last month.


I want to know: What factors influence this variable the most?
*graph of relative influence on accuracy
Can I build a model to predict who will leave and who will stay?
Can I apply this model to the onboarding process to a) make more accurate revenue predictions, and b)focus energy on retaining certain groups?
Is there enough evidence to warrant marketing to a specific customer subset? I should relate this to any data there is about who my customer base currently is...
Why do I see the results I'm seeing and can I influence them for the better?

Based on these questions,

First priority is interpretability and data display
second priority is model accuracy

throughout the process, think of what I would like to demonstrate/illustrate about the data.

customerID
Customer ID

gender
Whether the customer is a male or a female

SeniorCitizen
Whether the customer is a senior citizen or not (1, 0)

Partner
Whether the customer has a partner or not (Yes, No)

Dependents
Whether the customer has dependents or not (Yes, No)

tenure
Number of months the customer has stayed with the company
*graph the distribution and interpret how old the customer base is
PhoneService
Whether the customer has a phone service or not (Yes, No)

MultipleLines
Whether the customer has multiple lines or not (Yes, No, No phone service)

InternetService
Customer’s internet service provider (DSL, Fiber optic, No)

OnlineSecurity
Whether the customer has online security or not (Yes, No, No internet service)

OnlineBackup
Whether the customer has online backup or not (Yes, No, No internet service)

DeviceProtection
Whether the customer has device protection or not (Yes, No, No internet service)

TechSupport
Whether the customer has tech support or not (Yes, No, No internet service)

StreamingTV
Whether the customer has streaming TV or not (Yes, No, No internet service)

StreamingMovies
Whether the customer has streaming movies or not (Yes, No, No internet service)

Contract
The contract term of the customer (Month-to-month, One year, Two year)

PaperlessBilling
Whether the customer has paperless billing or not (Yes, No)

PaymentMethod
The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))

MonthlyCharges
The amount charged to the customer monthly

TotalCharges
The total amount charged to the customer

Churn
Whether the customer churned or not (Yes or No)

'''

'''
are senior citizensmore likely to stay or not?
-I'd really like to see each of these in chart to see which has a big impact - its a great set because it requires a lot of teasing apart'

'''



# Convert TotalCharges to numeric, coerce errors
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Remove rows with missing TotalCharges
df.dropna(subset=['TotalCharges'], inplace=True)

'''

from ehre we must proceed systematically, overview, then systematic zoom in. then machine learning.
'''

if __name__ == '__main__':
    print('running main')
    print('done')