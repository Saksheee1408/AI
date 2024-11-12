# First, let's print the columns to see what we're working with
print("All columns in the dataset:", data.columns.tolist())

# Now the corrected code
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Load data
data = pd.read_csv('/content/housing.csv')
features = ['RM', 'LSTAT', 'PTRATIO']  # Make sure these columns exist in your dataset
X =
data[features]
y = data['MEDV']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate error
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("\nMean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)

# Create new house data
new_house = np.array([[7, 10, 15]])  # Example values for RM, LSTAT, PTRATIO
predicted_price = model.predict(new_house)
print("\nPredicted Price for new house:", predicted_price[0])