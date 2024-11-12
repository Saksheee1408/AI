data=pd.read_csv('iris.csv')
print("\nFirst 5 rows of our data")
data.head()
print("\nBasic Information About Our Dataset:")
data.info()
print("\nLooking For missing values:")
print("-------------------------------")
missing_values=data.isnull().sum()
print(missing_values)
print("Finding Outliers:")

for column in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']:
        mean=data[column].mean()
        std=data[column].std()
        #Find Outliers(Values more than std deviations away from mean)
        outliers=data[abs(data[column]-mean)>2*std]
        outliers = data[abs(data[column] - mean) > 2*std]
    
        print(f"\nOutliers in {column}:")
        print(f"Number of outliers: {len(outliers)}")

       #Replace Outliers with mean value
        data.loc[abs(data[column] - mean)>2*std,column]=mean
print("\nSimple Transformation:")
print("-------------------------")
data['sepal_length_transformed']=np.sqrt(data['sepal_length'])
print("\nOriginal vs Transformed sepal_length (first 5 rows):")
print(data[['sepal_length', 'sepal_length_transformed']].head())
print("\nConverting categories into numbers:")
print("--------------------------------------")
species_numbers={
    'setosa':0,
    'versicolor':1,
    'virginica':2
}
data['species_numeric'] = data['species'].map(species_numbers)

print("\nFirst 5 rows showing species and their numbers:")
print(data[['species', 'species_numeric']].head())

