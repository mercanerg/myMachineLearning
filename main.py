import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read data from cvs file and catogorize non-numeric fields
data = pd.read_csv('data\insurance.csv')
data['sex'] = data['sex'].astype('category')
data['smoker'] = data['smoker'].astype('category')
data['region'] = data['region'].astype('category')

# This can be used to group large amounts of data and compute operations on these groups.
smoke_data = data.groupby('smoker').mean().round(2)

# visualize data in charts
sns.set_style('whitegrid')
sns.pairplot(data[["age", "bmi", "charges", "smoker"]],
             hue = 'smoker', height = 3, palette = "Set1")
sns.heatmap(data.corr(), annot = True)

# Dummy data is mock data generated at random as a substitute for live data in testing environments.
data = pd.get_dummies(data)
print("\n columns > ", data.columns)

# show charts
plt.show()