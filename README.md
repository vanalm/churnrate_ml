# Automated Exploratory Data Analysis Report

## Key Takeaways

- The higher the monthly bill, the higher the churn rate
- Categorical variables like contract type, online security, and internet service show strong associations with churn, with month-to-month contracts, lack of online security, and fiber optic service users being more likely to churn ( Chi-squared tests confirm these associations, and T-tests for numerical variables indicate significant differences between churn and non-churn groups.)
- This is an imbalanced dataset, treat it accordingly... (SMOTE or classweighting)
(>>> df['Churn'].value_counts(normalize=True)
Churn
No     0.73463
Yes    0.26537

### Business Conclusions:

1. **Focus on Retaining Month-to-Month Customers**  
   Churn is noticeably higher for customers on month-to-month contracts. Offering incentives like discounts or longer-term perks could help reduce churn in this group.

2. **Enhance Online Security and Tech Support Offerings**  
   Customers without online security or tech support services are more likely to leave. Consider bundling these services or offering them at a lower price to boost retention.

3. **Target High-Paying Customers for Retention**  
   Customers with higher monthly charges tend to churn more. Offering loyalty rewards or creating tailored packages for this segment could help keep them engaged.

4. **Prioritize Fiber-Optic Users**  
   Fiber-optic users show a higher churn rate. Focusing on service improvements or special promotions for these customers could help retain them.

5. **Address Churn in Electronic Check Payments**  
   Customers paying via electronic check churn the most. Maybe encouraging a switch to more stable payment methods with incentives or better user experience might help? Be sure to check other associations with electric payments too...

### Motivation for Predictive Modeling and Interpretability

1. **Predictive Modeling**:  
   Creating a churn prediction model helps businesses proactively identify at-risk customers, allowing for timely interventions and retention efforts, ultimately reducing churn rates.

2. **Interpretability**:  
   A focus on model interpretability enables better understanding of key factors driving churn, guiding data-driven decision-making and refining strategies for customer retention and service improvement.

---

## Data Processing Recommendations
- **Address Class Imbalance**: The churn class is imbalanced, must deal appropriately -> oversampling (SMOTE) or class weighting in models.
- **Handle Missing Data**: No missing values in this dataset
- **Standardization**: Standardize tenure, MonthlyCharges, and TotalCharges for better model performance, as they have different scales.
- **Encode Categorical Variables**: Use one-hot encoding for categorical variables like InternetService, Contract, PaymentMethod, and others.
- **Feature Engineering**: Create interaction terms or binary flags for customers with no online security or tech support, as these have strong associations with churn.

---

## Algorithm Recommendations
- **Logistic Regression**: A good starting point given the binary nature of the target variable (Churn), especially after feature scaling and one-hot encoding.
- **Random Forest / Gradient Boosting**: These ensemble methods can capture non-linear relationships and interactions between features effectively.
- **XGBoost**: (Good for handling imbalanced data)
- **Support Vector Machine (SVM)**: Useful for classification tasks, (scaling the features is important here
- **Neural Networks**: Applicable if the dataset is large enough, especially after transforming categorical variables into the rihgt format

## Numerical Variables Analysis

### Correlation with Target Variable (Churn):
- **Tenure**: -0.353 (Moderate negative correlation)
- **TotalCharges**: -0.198 (Weak negative correlation)
- **MonthlyCharges**: 0.194 (Weak positive correlation)
- **SeniorCitizen**: 0.151 (Weak positive correlation)

---

## Summary Statistics Grouped by Churn

### SeniorCitizen:
- Mean Churn: Yes = 0.26, No = 0.13 (Churn group has more senior citizens)

### Tenure:
- Mean Churn: Yes = 18.09, No = 37.72 (Lower tenure correlates with higher churn)

### MonthlyCharges:
- Mean Churn: Yes = 74.60, No = 61.39 (Higher charges correlate with higher churn)

### TotalCharges:
- Mean Churn: Yes = 1541.38, No = 2560.26 (Lower total charges correlate with higher churn)

---

## Categorical Variables Analysis

### Gender
- **Chi-Squared Test**: χ² = 0.4912, p = 0.4834 (Not significant)
- **Conclusion**: No significant relationship between gender and churn.

### Partner
- **Chi-Squared Test**: χ² = 154.27, p = 2.02e-35 (Highly significant)
- **Cramér's V**: 0.148 (Moderate association)
- **Conclusion**: Having a partner is moderately related to churn.

### Dependents
- **Chi-Squared Test**: χ² = 184.0, p = 6.49e-42 (Highly significant)
- **Cramér's V**: 0.162 (Moderate association)
- **Conclusion**: Customers without dependents are more likely to churn.

### PhoneService
- **Chi-Squared Test**: χ² = 0.7767, p = 0.3782 (Not significant)
- **Conclusion**: No significant relationship between phone service and churn.

### MultipleLines
- **Chi-Squared Test**: χ² = 12.30, p = 0.0021 (Significant)
- **Cramér's V**: 0.038 (Weak association)
- **Conclusion**: Multiple lines have a weak association with churn.

### InternetService
- **Chi-Squared Test**: χ² = 728.44, p = 6.61e-159 (Highly significant)
- **Cramér's V**: 0.322 (Relatively strong association)
- **Conclusion**: Internet service type strongly correlates with churn, particularly fiber-optic users.

### OnlineSecurity
- **Chi-Squared Test**: χ² = 843.47, p = 6.98e-184 (Highly significant)
- **Cramér's V**: 0.346 (Relatively strong association)
- **Conclusion**: Lack of online security services strongly correlates with churn.

### TechSupport
- **Chi-Squared Test**: χ² = 821.73, p = 3.66e-179 (Highly significant)
- **Cramér's V**: 0.342 (Relatively strong association)
- **Conclusion**: Customers without tech support are more likely to churn.

### Contract
- **Chi-Squared Test**: χ² = 1174.77, p = 7.99e-256 (Highly significant)
- **Cramér's V**: 0.409 (Relatively strong association)
- **Conclusion**: Contract type is a strong predictor of churn, with month-to-month customers showing higher churn rates.

### PaperlessBilling
- **Chi-Squared Test**: χ² = 253.57, p = 4.34e-57 (Highly significant)
- **Cramér's V**: 0.19 (Moderate association)
- **Conclusion**: Paperless billing moderately correlates with churn.

### PaymentMethod
- **Chi-Squared Test**: χ² = 641.20, p = 1.18e-138 (Highly significant)
- **Cramér's V**: 0.302 (Relatively strong association)
- **Conclusion**: Payment method strongly correlates with churn, with electronic check users having the highest churn rate.

---

## Numerical Variables Tests

### SeniorCitizen
- **T-test**: t = -11.35, p = 3.57e-29 (Highly significant)
- **Cohen's D**: -0.347 (Moderate effect size)

### Tenure
- **T-test**: t = 34.82, p = 2.91e-232 (Highly significant)
- **Cohen's D**: 0.856 (Large effect size)
- **Conclusion**: Longer tenure significantly reduces churn likelihood.

### MonthlyCharges
- **T-test**: t = -18.45, p = 4.29e-73 (Highly significant)
- **Cohen's D**: -0.448 (Moderate effect size)

### TotalCharges
- **T-test**: t = 18.66, p = 1.50e-74 (Highly significant)
- **Cohen's D**: 0.459 (Moderate effect size)

