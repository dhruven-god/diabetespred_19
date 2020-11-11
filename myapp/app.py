
import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

diabetes = pd.read_csv('C:\\Users\\dhruven\\ML\\diabetes.csv')


# Replacing the 0 values from ['Glucose','BloodPressure','SkinThickness','Insulin','BMI'] by NaN as there cannot be 0 in these features
diabetes_copy = diabetes.copy(deep=True)
diabetes_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)

# Replacing NaN value by mean, median as per distribution
diabetes_copy['Glucose'].fillna(diabetes_copy['Glucose'].median(), inplace=True)

diabetes_copy['BloodPressure'].fillna(diabetes_copy['BloodPressure'].median(), inplace=True)

diabetes_copy['SkinThickness'].fillna(diabetes_copy['SkinThickness'].mean(), inplace=True)
diabetes_copy['Insulin'].fillna(diabetes_copy['Insulin'].mean(), inplace=True)

diabetes_copy['BMI'].fillna(diabetes_copy['BMI'].median(), inplace=True)


X = df.drop(df['Outcome'])
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)



rf = RandomForestClassifier(n_estimators=20)
rf.fit(X_train, y_train)

filename = 'model.pkl'
pickle.dump(rf, open(filename, 'wb'))