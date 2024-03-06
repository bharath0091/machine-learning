# Simple Linear Regression

# Importing the libraries
import pandas as pd

# Importing the dataset
data = pd.read_csv("Icecream_Data.csv")
X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regress = LinearRegression()
regress.fit(X_train, Y_train)
regress.pl

# Predicting the Test set results


# Visualising the Training set results


# Visualising the Test set results
