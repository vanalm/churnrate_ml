# preprocess.py

'''
This is a goal of this script is to lay out a system of functions to preprocess a dataset, including the following steps:
1. Load the dataset
2. Clean the dataset
3. Split the dataset into training and testing sets
4. call either normalize or standardize functions, taking in and fitting first the training set, and allowing the ipnut of the fit transformer to operate on the test set
4. Normalize the dataset for knn, svm, neural networks, etc (distance metric based algorithms)
5. Standardize the dataset for linear regression, logistic regression, decision trees, PCA et ()
5. perform any feature engineering
6. Save the preprocessed dataset

subject to change as I get my hands dirty 

Linear Regression notes!
- Linear regression is sensitive to the scale of the input data
- sensitive to outliers, 
- sensitive to multicollinearity
- PolynomialFeatures can be used to create new features and campture nonlinearity in a linear regression model, but this can lead to overfitting
- Regularization can be used to prevent overfitting
- use pipelines to chain together multiple transformers and estimators, this allows more easy hyperparameter tuning and cross validation
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, Normalizer, OneHotEncoder, LabelEncoder, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, LogisticRegression
