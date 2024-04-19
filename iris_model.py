# iris_model.py

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Function to predict
def predict_iris(sep_length, sep_width, pet_length, pet_width):
    features = np.array([[sep_length, sep_width, pet_length, pet_width]])
    prediction = model.predict(features)
    iris_type = 'Setosa' if prediction[0] == 0 else ('Versicolor' if prediction[0] == 1 else 'Virginica')
    result_message = f"Your input values are: <br>Sepal Length: {sep_length}<br>Sepal Width: {sep_width}<br>Petal Length: {pet_length}<br>Petal Width: {pet_width}<br><span style='color:red;'>Forecast Result is: {iris_type}</span>"
    return result_message, iris_type
