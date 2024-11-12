# Import only what we need
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 1: Load data
data = pd.read_csv('sample_sales_data.csv')

# Step 2: Take only two columns for simple analysis
X = data[['QUANTITYORDERED', 'PRICEEACH']]

# Step 3: Elbow Method - Try clusters 1 to 5
elbow_scores = []  # Store scores here

for k in range(1, 6):  # Try only 1 to 5 clusters for simplicity
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    elbow_scores.append(kmeans.inertia_)
    print(f"Clusters {k}: Score {kmeans.inertia_:.0f}")

# Step 4: Plot Elbow Graph
plt.plot(range(1, 6), elbow_scores, 'bo-')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.show()

# Step 5: Create final clusters (let's use 3)
kmeans = KMeans(n_clusters=3)
data['Group'] = kmeans.fit_predict(X)

# Step 6: Show clusters in a scatter plot
plt.scatter(data['QUANTITYORDERED'], data['PRICEEACH'], c=data['Group'])
plt.title('Sales Groups')
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.show()

# Step 7: Print simple summary
for group_number in [0, 1, 2]:
    # Filter data for current group
    group_data = data[data['Group'] == group_number]
    
    # Calculate statistics
    order_count = len(group_data)
    avg_quantity = group_data['QUANTITYORDERED'].mean()
    avg_price = group_data['PRICEEACH'].mean()
    
    # Print results
    print(f"\nGroup {group_number + 1}:")
    print(f"Orders: {order_count}")
    print(f"Average Quantity: {avg_quantity:.0f}")
    print(f"Average Price: ${avg_price:.2f}")