import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset for demonstration
data = {
    'Age': np.random.randint(18, 65, 100),
    'Income': np.random.randint(20000, 80000, 100),
    'Education': np.random.randint(1, 5, 100),
    'Satisfaction': np.random.randint(1, 11, 100)
}

df = pd.DataFrame(data)

# Introduction to Data Visualization Libraries
# Basic Scatter Plot
plt.scatter(df['Age'], df['Income'])
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Scatter Plot of Age vs. Income')
plt.show()

# Basic Bar Plot
plt.bar(df['Education'], df['Satisfaction'])
plt.xlabel('Education Level')
plt.ylabel('Satisfaction Level')
plt.title('Bar Plot of Education Level vs. Satisfaction Level')
plt.show()

# Customizations
# Adding Colors and Labels to the Scatter Plot
plt.scatter(df['Age'], df['Income'], c='green', marker='o', label='Data Points')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Scatter Plot of Age vs. Income (Customized)')
plt.legend()
plt.show()

# Advanced Visualization for AI Data Representation
# Pairplot using Seaborn
sns.pairplot(df, hue='Education', palette='coolwarm', markers='o')
plt.title('Pairplot of Age, Income, Education, and Satisfaction')
plt.show()

# Heatmap using Seaborn
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu')
plt.title('Correlation Heatmap')
plt.show()
