<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Automated Integrated Analysis Report</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        h1 {
            color: #333;
        }

        h2 {
            color: #555;
            border-bottom: 1px solid #ccc;
            padding-bottom: 5px;
        }

        h3 {
            color: #666;
            margin-top: 30px;
        }

        h4 {
            color: #777;
            margin-top: 20px;
        }

        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
        }

        th,
        td {
            text-align: right;
            padding: 8px;
            border: 1px solid #ddd;
        }

        th {
            background-color: #f2f2f2;
        }

        img {
            max-width: 100%;
            height: auto;
            margin-bottom: 20px;
        }

        .section {
            margin-bottom: 60px;
        }

        .stat {
            font-weight: bold;
        }

        p {
            line-height: 1.6;
        }
    </style>
</head>

<body>
    <h1>Integrated Analysis Report</h1>



    <h2>Statistical Summary</h2>
    <p>
        The analysis reveals significant relationships between several factors and customer churn. Notably, longer tenure and higher total charges are associated with lower churn rates, while higher monthly charges slightly increase churn likelihood. Categorical variables such as contract type, online security, and internet service exhibit strong associations with churn, with month-to-month contracts, lack of online security, and fiber optic service users being more likely to churn. Chi-squared tests confirm these associations, and T-tests for numerical variables indicate significant differences between churn and non-churn groups.
    </p>

    <h2>Numerical Variables Analysis</h2>
    <h3>Correlation Analysis</h3>
    <h4>Correlation with Target Variable (Churn)</h4>
    <ul>
        <li>Tenure: -0.353 (Moderate negative correlation)</li>
        <li>TotalCharges: -0.198 (Weak negative correlation)</li>
        <li>MonthlyCharges: 0.194 (Weak positive correlation)</li>
        <li>SeniorCitizen: 0.151 (Weak positive correlation)</li>
    </ul>

    <h3>Summary Statistics Grouped by Churn</h3>
    <h4>SeniorCitizen:</h4>
    <p>Mean Churn: Yes = 0.26, No = 0.13 (Churn group has more senior citizens)</p>

    <h4>Tenure:</h4>
    <p>Mean Churn: Yes = 18.09, No = 37.72 (Lower tenure correlates with higher churn)</p>

    <h4>MonthlyCharges:</h4>
    <p>Mean Churn: Yes = 74.60, No = 61.39 (Higher charges correlate with higher churn)</p>

    <h4>TotalCharges:</h4>
    <p>Mean Churn: Yes = 1541.38, No = 2560.26 (Lower total charges correlate with higher churn)</p>

    <h2>Categorical Variables Analysis</h2>

    <h3>Gender</h3>
    <p>Chi-Squared Test: χ² = 0.4912, p = 0.4834 (Not significant)</p>
    <p>Conclusion: No significant relationship between gender and churn.</p>

    <h3>Partner</h3>
    <p>Chi-Squared Test: χ² = 154.27, p = 2.02e-35 (Highly significant)</p>
    <p>Cramér's V: 0.148 (Moderate association)</p>
    <p>Conclusion: Having a partner is moderately related to churn.</p>

    <h3>Dependents</h3>
    <p>Chi-Squared Test: χ² = 184.0, p = 6.49e-42 (Highly significant)</p>
    <p>Cramér's V: 0.162 (Moderate association)</p>
    <p>Conclusion: Customers without dependents are more likely to churn.</p>

    <h3>PhoneService</h3>
    <p>Chi-Squared Test: χ² = 0.7767, p = 0.3782 (Not significant)</p>
    <p>Conclusion: No significant relationship between phone service and churn.</p>

    <h3>MultipleLines</h3>
    <p>Chi-Squared Test: χ² = 12.30, p = 0.0021 (Significant)</p>
    <p>Cramér's V: 0.038 (Weak association)</p>
    <p>Conclusion: Multiple lines have a weak association with churn.</p>

    <h3>InternetService</h3>
    <p>Chi-Squared Test: χ² = 728.44, p = 6.61e-159 (Highly significant)</p>
    <p>Cramér's V: 0.322 (Relatively strong association)</p>
    <p>Conclusion: Internet service type strongly correlates with churn, particularly fiber-optic users.</p>

    <h3>OnlineSecurity</h3>
    <p>Chi-Squared Test: χ² = 843.47, p = 6.98e-184 (Highly significant)</p>
    <p>Cramér's V: 0.346 (Relatively strong association)</p>
    <p>Conclusion: Lack of online security services strongly correlates with churn.</p>

    <h3>TechSupport</h3>
    <p>Chi-Squared Test: χ² = 821.73, p = 3.66e-179 (Highly significant)</p>
    <p>Cramér's V: 0.342 (Relatively strong association)</p>
    <p>Conclusion: Customers without tech support are more likely to churn.</p>

    <h3>Contract</h3>
    <p>Chi-Squared Test: χ² = 1174.77, p = 7.99e-256 (Highly significant)</p>
    <p>Cramér's V: 0.409 (Relatively strong association)</p>
    <p>Conclusion: Contract type is a strong predictor of churn, with month-to-month customers showing higher churn rates.</p>

    <h3>PaperlessBilling</h3>
    <p>Chi-Squared Test: χ² = 253.57, p = 4.34e-57 (Highly significant)</p>
    <p>Cramér's V: 0.19 (Moderate association)</p>
    <p>Conclusion: Paperless billing moderately correlates with churn.</p>

    <h3>PaymentMethod</h3>
    <p>Chi-Squared Test: χ² = 641.20, p = 1.18e-138 (Highly significant)</p>
    <p>Cramér's V: 0.302 (Relatively strong association)</p>
    <p>Conclusion: Payment method strongly correlates with churn, with electronic check users having the highest churn rate.</p>

    <h2>Numerical Variables Tests</h2>

    <h3>SeniorCitizen</h3>
    <p>T-test: t = -11.35, p = 3.57e-29 (Highly significant)</p>
    <p>Cohen's D: -0.347 (Moderate effect size)</p>

    <h3>Tenure</h3>
    <p>T-test: t = 34.82, p = 2.91e-232 (Highly significant)</p>
    <p>Cohen's D: 0.856 (Large effect size)</p>
    <p>Conclusion: Longer tenure significantly reduces churn likelihood.</p>

    <h3>MonthlyCharges</h3>
    <p>T-test: t = -18.45, p = 4.29e-73 (Highly significant)</p>
    <p>Cohen's D: -0.448 (Moderate effect size)</p>

    <h3>TotalCharges</h3>
    <p>T-test: t = 18.66, p = 1.50e-74 (Highly significant)</p>
    <p>Cohen's D: 0.459 (Moderate effect size)</p>

    <h2>Data Processing Recommendations</h2>
    <ul>
        <li>Handle Missing Data: Impute or remove missing values, especially in continuous variables like TotalCharges.</li>
        <li>Standardization: Standardize tenure, MonthlyCharges, and TotalCharges for better model performance, as they have different scales.</li>
        <li>Encode Categorical Variables: Use one-hot encoding for categorical variables like InternetService, Contract, PaymentMethod, and others.</li>
        <li>Feature Engineering: Create interaction terms or binary flags for customers with no online security or tech support, as these have strong associations with churn.</li>
        <li>Address Class Imbalance: If the churn class is imbalanced, apply techniques such as oversampling (SMOTE) or class weighting in models.</li>
    </ul>

    <h2>Algorithm Recommendations</h2>
    <ul>
        <li>Logistic Regression: A good starting point given the binary nature of the target variable (Churn), especially after feature scaling and one-hot encoding.</li>
        <li>Random Forest / Gradient Boosting: These ensemble methods can capture non-linear relationships and interactions between features effectively.</li>
        <li>XGBoost: Ideal for handling imbalanced data and extracting complex patterns.</li>
        <li>Support Vector Machine (SVM): Useful for classification tasks, though more appropriate after scaling the features.</li>
        <li>Neural Networks: Applicable if the dataset is large enough, especially after transforming categorical variables into suitable formats.</li>
    </ul>

</body>

</html>
